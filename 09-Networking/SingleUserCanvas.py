########################################
# SingleUserCanvas.py
# Author: Doug Galarus
########################################

import stddraw
    

#-----------------------------------------------------------------------

# main() method
def main():

    # Boolean flag to track clicks for line-drawing.
    # If True, the next click will define the start of a line segment.
    # If False, the next click will define the end of a line segment.
    startNewLine = True
    
    # Starting coordinates for line segment
    startX = 0.0
    startY = 0.0
    
    # End coordinates for line segment
    endX = 0.0
    endY = 0.0

    # Clear/initialize the stddraw window.
    stddraw.clear()
    
    # Set the pen color to black.
    stddraw.setPenColor(stddraw.BLACK)
    
    # Print simple instructions.
    print('------------------------------------------------------------------')
    print('Single User Canvas')
    print('------------------------------------------------------------------')
    print('Click the mouse to draw lines. The first click chooses the start,')
    print('the second chooses the end and draws the line segment on the canvas.')
    print('Type c to clear the canvas.')
    print('Type q to quit and exit the program.')
    print('------------------------------------------------------------------')
    
    # Infinite loop to process events.
    while True:
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
                stddraw.line(startX, startY, endX, endY)
                print(f"({startX}, {startY}) -> ({endX}, {endY})")
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
                stddraw.clear()
            # If it is a q, then quit the infinite loop via break.
            if ch == 'q':
                break
        # Show with 100 ms delay. The value could be decreased to be more responsive.
        stddraw.show(100)
    # Print exit message.
    print("Exiting Single User Canvas")

#-----------------------------------------------------------------------

# Call the main function when invoked.
if __name__ == '__main__':
    main()
