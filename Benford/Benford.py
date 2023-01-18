import sys

class Benford:
    def __init__(self):
        self.tally = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def countDigits(self, num):
        return len(str(num))

    def nthDigitBack(self, n, num):
        if len(str(num)) > n:
            return int(str(num)[len(str(num)) - 1 - n])
        return -1

    def nthDigit(self, n, num):
        if self.countDigits(num) > n:
            return self.nthDigitBack(self.countDigits(num) - 1 - n, num)
        return -1

    def nthDigitTally1(self, n, num, tally):
        numToIncrease = self.nthDigit(n, num)
        if not numToIncrease == -1:
            tally[numToIncrease] += 1
        return tally

    def nthDigitTally(self, n, nums):
        tally = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for num in nums:
            tally = self.nthDigitTally1(n, num, tally)
        return tally

    def readMysteriousNumbers(self, fName):
        data = []
        with open(fName, 'r') as f:
            for line in f:
                data.append(int(line))
        data.pop(0)
        return data

if __name__ == '__main__':
    ben = Benford()
    digit = int(sys.argv[1])
    filename = sys.argv[2]

    output = ['0s', '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s']
    data = ben.readMysteriousNumbers(filename)
    result = ben.nthDigitTally(digit, data)
    for item in output:
        print(f"{item}: {result[int(item[0])]}")
        
    # print(f"counting the {digit} digit in {filename}")
    # print(f"\nNumber of digits in 302: {ben.countDigits(302)}")

    # print(f"\n0 digit back in 123 is: {ben.nthDigitBack(0, 123)}")
    # print(f"1 digit back in 123 is: {ben.nthDigitBack(1, 123)}")
    # print(f"2 digit back in 123 is: {ben.nthDigitBack(2, 123)}")
    # print(f"3 digit back in 123 is: {ben.nthDigitBack(3, 123)}")
    # print(f"3 digit back in 18023 is: {ben.nthDigitBack(3, 18023)}")
    
    # print(f"\n0 digit in 123 is: {ben.nthDigit(0, 123)}")
    # print(f"1 digit in 123 is: {ben.nthDigit(1, 123)}")
    # print(f"2 digit in 123 is: {ben.nthDigit(2, 123)}")
    # print(f"3 digit in 123 is: {ben.nthDigit(3, 123)}")
    # print(f"3 digit in 18023 is: {ben.nthDigit(3, 18023)}")
    
    # enrollments = [12176, 5476, 543, 3490, 24892, 28619, 2595, 603, 2527, 1465, 1858]
    # print(f"\nUsing enrollments, nthDigitTally = {ben.nthDigitTally(0, enrollments)}")

    # nums = [123, 223, 323, 423, 523, 623456, 723, 823, 923]
    # print(f"Using (0, nums) nthDigitTally = {ben.nthDigitTally(0, nums)}")
    # print(f"Using (5, nums) nthDigitTally = {ben.nthDigitTally(5, nums)}")
    # print(f"Using (1, nums) nthDigitTally = {ben.nthDigitTally(1, nums)}")
    # print(f"Using (10, nums) nthDigitTally = {ben.nthDigitTally(10, nums)}")
