# Filename: 1000DigitFibonacci
# Description: Finds the first term in the Fibonacci sequence that
#              contains 1000 digits.

import sys
sys.dont_write_bytecode = True
sys.path.insert(0, '../LongestCollatzSequence/')
from LongestCollatzSeq import printList

# assumes that at least 2 elements are in fibonacci
def generateNextFib(fibonacci):
    oneBefore = fibonacci[len(fibonacci) - 1]
    twoBefore = fibonacci[len(fibonacci) - 2]
    return oneBefore + twoBefore

# converts num to string
# checks if string has greater than 3 chars
def lessThanFourDigits(num):
    numString = str(num)
    return (len(numString) < 1000)

def main():
    fibonacci = []
    fibonacci.append(1)
    fibonacci.append(1)
    while(lessThanFourDigits(fibonacci[len(fibonacci) - 1])):
        fibonacci.append(generateNextFib(fibonacci))
    print "The non-zeroed index of the first term in the Fibonacci sequence to contain 1000 digits is %d" % len(fibonacci)
    # printList(fibonacci)

if __name__ == "__main__":
    main()
