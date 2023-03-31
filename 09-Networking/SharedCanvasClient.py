########################################
# MAGIC8BALL_tcp_client.py
# Author: Doug Galarus
########################################

import socket
from datetime import datetime
import sys
import stddraw
import time
import os

# Maximum size (in bytes) to retrieve from server
max_size = 1048576

drawing = True

def connectToServer():
    global drawing
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
        return client
        
    # If an exception occurred in binding or initially trying to connect, print an error message and exit.
    except:
        print("An error occurred when attempting to connect to the server at the given address and port.")
        return

# main() method
def main():
    global drawing
    # Make sure the host argument is passed.
    # The host argument specifies the (local) host.
    # This can be localhost or 127.0.0.1 for the loopback address.
    # Or, it can be the IP address of the remote computer. This allows access to the server on other computers.
    if len(sys.argv) != 2:
        if ((len(sys.argv) == 3) and (sys.argv[2] == 'close')):
            drawing = False
        else:
            print("Usage: python MAGIC8BALL_tcp_client.py host")
            print("host may be localhost or the IP address bound to the (remote) host computer you are accessing.")
            return
    
    # Bind to the host and port and try to connect.
        
    try:
        client = connectToServer()
        # Send a request to the server.
        client.sendall(b'Hey!')
        # Get the response.
        data = client.recv(max_size)
        stddraw.clear()
        stddraw.setPenColor(stddraw.BLACK)
        startNewLine = True
        while drawing:
            client = connectToServer()
            # Check for mouse press/click.
            if stddraw.mousePressed():
                # Draw a point to show the user where the click was.
                stddraw.filledCircle(stddraw.mouseX(), stddraw.mouseY(), .005)
                # Handle case where mouse click indicates end of line.
                if startNewLine == False:
                    # Get the end coordinates.
                    endX = stddraw.mouseX()
                    endY = stddraw.mouseY()
                    # Draw the line segment.
                    lineToSend = f"ADD {startX} {startY} {endX} {endY}"
                    # print("Sending line")
                    client.sendall(bytes(lineToSend, 'utf-8'))
                    # print("\tSent!")
                    # Set flag to start new line on next mouse click.
                    startNewLine = True
                # Handle case where mouse click indicates start of line.
                else:
                    # Get the start coordinates.
                    startX = stddraw.mouseX()
                    startY = stddraw.mouseY()
                    # Set flag to end line on next mouse click.
                    startNewLine = False
            # Check for key press.
            if stddraw.hasNextKeyTyped():
                # Retrieve the character.
                ch = stddraw.nextKeyTyped()
                # If it is a c, clear the canvas.
                if ch == 'c':
                    client.sendall(bytes("CLEAR", 'utf-8'))
                # If it is a q, then quit the infinite loop via break.
                if ch == 'q':
                    client.sendall(bytes("QUIT", 'utf-8'))
                    break
                if ch == 'z':
                    client.sendall(bytes("CLOSE", 'utf-8'))
                    break
            # Show with 100 ms delay. The value could be decreased to be more responsive.
            stddraw.show(100)
            
            print("Sending GET")
            client.sendall(bytes("GET", 'utf-8'))
            print("\tSent!")
            data = client.recv(max_size)
            print("Data recieved")
            # Decode the response as a UTF-8 string.
            strResponse = data.decode("UTF-8")
            lines = strResponse.split(" ")
            # print(lines)
            numOfLines = int(lines[0])
            for i in range(numOfLines):
                startIndex = (i * 4) + 1
                x1 = float(lines[startIndex])
                y1 = float(lines[startIndex + 1])
                x2 = float(lines[startIndex + 2])
                y2 = float(lines[startIndex + 3])
                stddraw.line(x1, y1, x2, y2)
            # client.close()
        client.close()


    # If and exception occurs, print an error message and return.
    except Exception as e:
        print("An error occurred when making a request to the server.")
        print(f"ERROR: {e}")
        # Close the connection to the server.
        client.close()
        return


# Call the main function when invoked.
if __name__ == "__main__":
    main()
    