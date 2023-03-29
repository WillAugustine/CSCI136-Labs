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
fortunes = ["It is certain.",
			"It is decidedly so.",									
			"Without a doubt.",
			"Yes, definitely.",
			"You may rely on it.",
			"As I see it, yes.",
			"Most likely.",
			"Outlook good.",
			"Yes.",
			"Signs point to yes.",
			"Reply hazy, try again.",
			"Ask again later.",
			"Better not tell you now.",
			"Cannot predict now.",
			"Concentrate and ask again.",
			"Don't count on it.",
			"My reply is no.",
			"My sources say no.",
			"Outlook not so good.",
			"Very doubtful."]

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
    # Prints that a request has been received.
    # Print the time, client information, and the data, decoded as a UTF-8 string.
    print('At', datetime.now(), client, 'said', data.decode("UTF-8"))
    # Randomly select a fortune.
    strTheFortune = fortunes[random.randrange(len(fortunes))]
    # Send the response to the client.
    strResponse = str(count) + ";" + strTheFortune
    client.sendall(bytes(strResponse, 'utf-8'))
    # Print the response.
    print('Response: ', strResponse)
    # Print the number of requests handled since the server started.
    print(str(count),"request(s) handled so far.")
    # Close the connection to the client.
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
        
        print('Starting the Magic 8 Ball server at:', datetime.now())
        
        # Create a socket.
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind to the address (host, port) combination.
        server.bind(address)
        # Listen for requests. Allow a "backlog" of 5, meaning roughly 5 simultaneous connections allowed.
        server.listen(5)
    # If an exception occurred in binding or initially trying to listen, print an error message and exit.
    except:
        print("An error occurred when attempting to bind to the address and port.")
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
    
    
    