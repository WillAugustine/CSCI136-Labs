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

port = 6789

host = ""

def connectSendRecieve(command):
    global drawing, port, host
    try:
        
        address = (host, port)
        
        # Create a socket.
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Try to connect to the server.
        client.connect(address)
        client.sendall(bytes(command, 'utf-8'))
        # Get the response.
        data = client.recv(max_size)
        # Decode the response as a UTF-8 string.
        response = data.decode("UTF-8")
        
        # Close the connection to the server.
        client.close()
        
        #print(strResponse)
        
        return response
        
    # If an exception occurred in binding or initially trying to connect, print an error message and exit.
    except:
        print("An error occurred when attempting to connect to the server at the given address and port.")
        return
    
def drawFromGet(command):
    stddraw.clear()
    lines = command.split(" ")
    # print(lines)
    numOfLines = int(lines[0])
    for i in range(numOfLines):
        startIndex = (i * 4) + 1
        x1 = float(lines[startIndex])
        y1 = float(lines[startIndex + 1])
        x2 = float(lines[startIndex + 2])
        y2 = float(lines[startIndex + 3])
        stddraw.line(x1, y1, x2, y2)


# main() method
def main():
    global drawing, port, host
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
        host = sys.argv[1]
        startX = 0.0
        startY = 0.0
        endX = 0.0
        endY = 0.0
        stddraw.clear()
        stddraw.setPenColor(stddraw.BLACK)
        startNewLine = True
        while drawing:
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
                    command = f"ADD {round(startX, 3)} {round(startY, 3)} {round(endX, 3)} {round(endY, 3)}"
                    # print("Sending line")
                    response = connectSendRecieve(command)
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
                ch = stddraw.nextKeyTyped().lower()
                # If it is a c, clear the canvas.
                if ch == 'c':
                    response = connectSendRecieve("CLEAR")
                # If it is a q, then quit the infinite loop via break.
                if ch == 'q':
                    response = connectSendRecieve("QUIT")
                    break
                if ch == 'z':
                    response = connectSendRecieve("CLOSE")
                    break
            # Show with 100 ms delay. The value could be decreased to be more responsive.
            stddraw.show(100)
            
            # print("Sending GET")
            response = connectSendRecieve("GET")
            drawFromGet(response)
            # print("\tSent!")
            
        connectSendRecieve("QUIT")


    # If and exception occurs, print an error message and return.
    except Exception as e:
        print("An error occurred when making a request to the server.")
        print(f"ERROR: {e}")
        return


# Call the main function when invoked.
if __name__ == "__main__":
    main()
    