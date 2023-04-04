########################################
# MAGIC8BALL_tcp_server.py
# Author: Doug Galarus
########################################

from datetime import datetime
import socket
import threading
import random
import stddraw
import sys
import os

# These are the 20 Magic 8 Ball responses:
lines = []

# Maximum size (in bytes) to retrieve from clients
max_size = 2000


# Lock for updating request counter.
lock = threading.Lock()

exitFlag = False

def GET():
    global lines
    lock.acquire()
    lineString = str(len(lines))
    for line in lines:
        currLine = f" {line['x1']} {line['y1']} {line['x2']} {line['y2']}"
        lineString += currLine
    lock.release()
    return lineString
    

def ADD(command):
    global lines
    stringRecieved = command.split(" ")
    x1 = float(stringRecieved[1])
    y1 = float(stringRecieved[2])
    x2 = float(stringRecieved[3])
    y2 = float(stringRecieved[4])
    lock.acquire()
    line = {
        'x1': x1,
        'y1': y1,
        'x2': x2,
        'y2': y2,
    }
    lines.append(line)
    lock.release()
    return "OK"

def CLEAR():
    global lines
    lock.acquire()
    lines.clear()
    lock.release()
    print(f"lines: {lines}")
    return "OK"

def QUIT():
    return "OK"

def CLOSE():
    global exitFlag
    exitFlag = True
    os.system('python SharedCanvasClient.py localhost close')
    return "\nStopping server..."

def processCommand(command, client):
    if (command[0:3] == "GET"):
        return GET()
    elif (command[0:3] == "ADD"):
        return ADD(command)
    elif (command[0:5] == "CLEAR"):
        print("Clearing...")
        return CLEAR()
    elif (command[0:4] == "QUIT"):
        print(f"GOODBYE: {client}")
        return QUIT()
    elif (command[0:5] == "CLOSE"):
        message = CLOSE()
        print(message)
        return message

# The client_thread() function processes individual client requests.   
# A client object is passed to the function.     
def client_thread(client):
    # Receive the request data (in bytes).
    data = client.recv(max_size)
    # print(f"data on server: {data}")
    command = data.decode("UTF-8")
    client.sendall(bytes(processCommand(command, client), 'utf-8'))
        
    client.close()



# main() method
def main():
    
    # Make sure the host argument is passed.
    # The host argument specifies the (local) host.
    # This can be localhost or 127.0.0.1 for the loopback address.
    # Or, it can be the IP address of the local computer. This allows access from other computers.
    if len(sys.argv) != 2:
        print("Usage: python MAGIC8BALL_tcp_server.py host")
        print("host may be localhost or an IP address bound to the local computer you are using.")
        return
    
    # Bind to the host and port and start listening.
    try:
        # Get the host command line argument.
        host = sys.argv[1]
        # Hard-coded port for this application.
        port = 6789
        
        address = (host, port)
        
        print('Starting the shared canvas server at:', datetime.now())
        
        # Create a socket.
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind to the address (host, port) combination.
        server.bind(address)
        # Listen for requests. Allow a "backlog" of 5, meaning roughly 5 simultaneous connections allowed.
        server.listen(5)
        
    # If an exception occurred in binding or initially trying to listen, print an error message and exit.
    except Exception as e:
        print("An error occurred when attempting to bind to the address and port.")
        print(f"ERROR: {e}")
        return
    
    # Now wait for client requests.
    print('Waiting for clients to make requests.')
    while not exitFlag:
        # Block and wait for a client request.
        client, addr = server.accept()
        print(f"HELLO: {client}")
        # Create and start a new client_thread to handle the request.
        p = threading.Thread(target=client_thread, args=(client,))
        p.start()
        # print(f"exitFlag at end of while loop: {exitFlag}")
    

    # Close the server.
    # This line will not be reached, because there is no mechanism to exit the infinite loop above.
    server.close()


# Call the main function when invoked.
if __name__ == "__main__":
    main()
    
    
    