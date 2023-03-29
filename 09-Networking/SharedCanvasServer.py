########################################
# MAGIC8BALL_tcp_server.py
# Author: Doug Galarus
########################################

from datetime import datetime
import socket
import threading
import random
import sys

# These are the 20 Magic 8 Ball responses:
lines = []

# Maximum size (in bytes) to retrieve from clients
max_size = 1000

# Request counter.
requestCount = 0

# Lock for updating request counter.
lock = threading.Lock()


# The client_thread() function processes individual client requests.   
# A client object is passed to the function.     
def client_thread(client): 
    # Update the request count, the number of requests the server has handled.
    global requestCount
    global lock
    # Lock to avoid concurrency issues.
    lock.acquire()
    requestCount = requestCount + 1
    # Grab a local copy since the global value could change before subsequent use.
    count = requestCount
    lock.release()
    
    # Receive the request data (in bytes).
    data = client.recv(max_size)
    # print(f"data on server: {data}")
    stringRecieved = data.decode("UTF-8").split(" ")
    # print(f"stringRecieved on server: {stringRecieved}")
    command = stringRecieved[0]
    # print(f"command on server: {command}")
    if command == "ADD":
        # print("Adding")
        x1 = stringRecieved[1]
        y1 = stringRecieved[2]
        x2 = stringRecieved[3]
        y2 = stringRecieved[4]
        line = {
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2,
        }
        lines.append(line)
    if command == "GET":
        lineString = str(len(lines))
        for line in lines:
            currLine = f" {line['x1']} {line['y1']} {line['x2']} {line['y2']}"
            lineString += currLine
        client.sendall(bytes(lineString, 'utf-8'))
    if command == "CLEAR":
        print("clear")
    if command == "QUIT":
        print("quit")
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
        
        print(f"HELLO: {server}")
    # If an exception occurred in binding or initially trying to listen, print an error message and exit.
    except Exception as e:
        print("An error occurred when attempting to bind to the address and port.")
        print(f"ERROR: {e}")
        return
    
    # Now wait for client requests.
    print('Waiting for clients to make requests.')
    while True:
        # Block and wait for a client request.
        client, addr = server.accept()
        # Create and start a new client_thread to handle the request.
        p = threading.Thread(target=client_thread, args=(client,))
        p.start()
    
    # Close the server.
    # This line will not be reached, because there is no mechanism to exit the infinite loop above.
    server.close()


# Call the main function when invoked.
if __name__ == "__main__":
    main()
    
    
    