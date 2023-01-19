# -----------------------------------------------------------------------------
# 
# File Name: Benford.py
#
# Author: Jason Decker
#
# Description:  Program that determines the distribution of initial digits in
#               a set of data. 
#
# How to use:   Import into another file with "import Benford as B" 
#               or similar. Then create instances of the class and use them.
#
#               import Benford as B
#                    
#               Benford1 = B.Benford()
#               print(Benford1)
#
# -----------------------------------------------------------------------------
import sys
# ----------------------------------------------------------------------------
# Define the Benford Class
# ----------------------------------------------------------------------------
class Benford:
    
    # ----------------------------------------------------------------------------
    # Initialization Method: __init__()
    #
    # Inputs:
    #   self: reference the object
    # 
    # Return Value:
    #   __init__() does not return a value.
    #
    # Example Use:
    #   Note: __init__() is not called directly. It's called when the constructor
    #         is called, after space has been allocated for the object.
    #
    # Description:
    #   Initialize member of the class.
    #
    # ----------------------------------------------------------------------------
    def __init__(self):
        pass

    # ----------------------------------------------------------------------------
    # Instance Method: countDigits(num) 
    #
    # Inputs:
    #   self: reference to object
    #   num: integer system input argument
    #
    # Return Value:
    #   Method calculates and returns the number of digits in the integer input argument, num.
    # ----------------------------------------------------------------------------
    def countDigits(self, num):
        length = len(str(num))
        return length
    
    # ----------------------------------------------------------------------------
    # Method: nthDigitBack(n,num) 
    #
    # Inputs:
    #   self: reference to object
    #   num: integer system input argument
    #   n: integer system input argument for the nth digit from the right.
    #
    # Return Value:
    #   Returns an integer digit at the nth position from the right from the number num.
    # ----------------------------------------------------------------------------
    def nthDigitBack(self,n,num):
        index = n
        number = str(num)
        # DigitBack calls the number and finds the digit based on the indexing from the right
        if index < len(number):
            DigitBack = int(number[len(number)-1-n])
            #print(DigitBack)
            return DigitBack
        return -1 
        
        
    # ----------------------------------------------------------------------------
    # Method: nthDigit(n,num) 
    #
    # Inputs:
    #   self: reference to object
    #   num: integer system input argument
    #   n: integer system input argument for the nth digit from the left.
    #
    # Return Value:
    #   Returns the integer digit at the nth position from the left from the number num.
    # ----------------------------------------------------------------------------
    
    def nthDigit(self,n,num):
        if self.countDigits(num) > n:
            return self.nthDigitBack(self.countDigits(num) - 1 - n, num)
        return -1
        # length = self.countDigits(num)
        # index = self.nthDigitBack(length-1-n,num)
        # #if length <= n:
        # #    return -1
        # return index

    # ----------------------------------------------------------------------------
    # Method: nthDigitTally1(n,num,tally) 
    #
    # Inputs:
    #   self: reference to object
    #   num: integer system input argument
    #   n: integer system input argument for the nth digit from the left.
    #   tally: list system input argument representing the count of each digit
    #          tallied so far.
    #
    # Return Value:
    #   Updates and returns the tally list with a new count based on the 
    #   corresponding digit n in the number num.
    # ----------------------------------------------------------------------------
    def nthDigitTally1(self,n,num,tally):
        index = self.nthDigit(n, num)
        if not index == -1:
            tally[index] += 1
        return tally

    # ----------------------------------------------------------------------------
    # Method: nthDigitTally(n,nums) 
    #
    # Inputs:
    #   self: reference to object
    #   nums: integer system input argument
    #   n: integer system input argument for the nth digit from the left
    #
    # Return Value:
    #   Returns a tally list of all the digits in the nth position.
    # ----------------------------------------------------------------------------
    def nthDigitTally(self,n,nums):
        tally = [0] * 10
        for number in nums:
            tally = self.nthDigitTally1(n, number, tally)
        print(len(tally))
        return tally

    # ----------------------------------------------------------------------------
    # Method: readMysteriousNumbers(Name) 
    #
    # Inputs:
    #   self: reference to object
    #   Name: input from text file
    #   
    # Return Value:
    #   Opens a file and returns all the numbers in a list. Assumes the first
    #   number is the count of the subsequent numbers in the file and does not
    #   include that in the list.
    # ----------------------------------------------------------------------------    
    def readMysteriousNumbers(self,Name):
        file = open(Name, 'rt')
        lines = file.read().splitlines()
        numbers = lines[1:]
        data = []
        for item in numbers:
            data.append(int(item))
        return data

# ----------------------------------------------------------------------------
# Main Function: main()
#   Main function that runs only if the script is directly executed.
#
# Inputs: 
#   n: integer number read by the function as a command line argument.
#   name: file name read by the function as a command line arguement.
#
# How to use:
#   python Benford.py n name
#       example: python Benford.py 0 TestData.txt
# ----------------------------------------------------------------------------

def main():
    #n = int(sys.argv[1])
    #name = sys.argv[2]

    B = Benford()
   # numbers = B.readMysteriousNumbers(name)
    #result = B.nthDigitTally(n, numbers)
    #indeces = [0,1,2,3,4,5,6,7,8,9]
    #tally = [0]*10
    #Test for countDigits
    #print(f"\nTest for countDigits, Number of digits in 8647 is (should be 4): {B.countDigits(8647)}")
    
    #Test for nthDigitBack
    #print(f"\nTest for nthDigitBack, 1 digit from the right in 1234 is (should be 3): {B.nthDigitBack(1, 1234)}")
    #print(f"\nTest for nthDigitBack, 0 digit from the fright in 1234 is (should be 4): {B.nthDigitBack(0, 1234)}")
    #print(B.nthDigitBack(0, 1234567890123456789012345678901234567890))
    
    #Test for nthDigit
    #print(f"\nTest for nthDigit, 0 digit in 1234 is (should be 1): {B.nthDigit(0, 1234)}")
    #print(f"\nTest for nthDigit, 2 digit in 1234 is (should be 3): {B.nthDigit(2, 1234)}")
        
    #Test for nthDigitTally1
    #print(f"\nTest for nthDigitTally1, 2 digit from 1072 with starting tally of [0,0,1,2,0,0,3,0,9,0]") 
    #print("(should be [0,0,1,2,0,0,3,1,9]): {B.nthDigitTally1(2, 1072, [0,0,1,2,0,0,3,0,9,0])}")
    #print({B.nthDigitTally1(2, 1072, tally)})
    
#Test for nthDigitTally
    #print(f"\nTest for nthDigitTally, 0 digit with TestData.txt (should be [0,3,4,1,0,2,1,0,0,0]:")
    print(B.nthDigitTally(5,[123, 223, 323, 423, 523, 623456, 723, 823, 923]))
    
#Test for readMysteriousNumbers
#print(f"Test for readMysteriousNumbers, TestData.txt: {B.readMysteriousNumbers('TestData.txt')}")

   
   # for index in indeces:
        #print(f"{index}s: {result[index]}")
if __name__ == '__main__':
    main()
