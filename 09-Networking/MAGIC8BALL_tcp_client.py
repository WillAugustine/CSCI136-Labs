########################################
# MAGIC8BALL_tcp_client.py
# Author: Doug Galarus
########################################

import socket
from datetime import datetime
import sys

# Maximum size (in bytes) to retrieve from server
max_size = 1000


# main() method
def main():
    
    # Make sure the host argument is passed.
    # The host argument specifies the (local) host.
    # This can be localhost or 127.0.0.1 for the loopback address.
    # Or, it can be the IP address of the remote computer. This allows access to the server on other computers.
    if len(sys.argv) != 2:
        print("Usage: python MAGIC8BALL_tcp_client.py host")
        print("host may be localhost or the IP address bound to the (remote) host computer you are accessing.")
        return
    
    # Bind to the host and port and try to connect.
    try:
        # Get the host command line argument.
        host = sys.argv[1]
        # Hard-coded port for this application.
        port = 6789
        
        address = (host, port)
        
        # Create a socket.
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Try to connect to the server.
        client.connect(address)
        
    # If an exception occurred in binding or initially trying to connect, print an error message and exit.
    except:
        print("An error occurred when attempting to connect to the server at the given address and port.")
        return
        
    try:
        # Send a request to the server.
        client.sendall(b'Hey!')
        # Get the response.
        data = client.recv(max_size)
        # Decode the response as a UTF-8 string.
        strResponse = data.decode("UTF-8")
        # Split the response on the semicolon to separate the count from the fortune.
        (strCount, strFortune) = strResponse.split(';')
        
        # Print the time and count.
        print('As of', datetime.now(), 'the Magic 8 Ball Server has made', strCount, 'prediction(s).')
        print('The Magic 8 Ball Server says:')
        # Print the fortune.
        print(strFortune)
        
        # Close the connection to the server.
        client.close()
    # If and exception occurs, print an error message and return.
    except:
        print("An error occurred when making a request to the server.")
        # Close the connection to the server.
        client.close()
        return


# Call the main function when invoked.
if __name__ == "__main__":
    main()
    