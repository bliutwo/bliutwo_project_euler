# File: PowerDigitSum.py
# Description: https://projecteuler.net/problem=16

def parseNum(num):
    parsedNum = []
    number_string = str(num)
    for ch in number_string:
        parsedNum.append(int(ch))
    return parsedNum

def getSumDigits(num):
    total = 0
    parsedNum = parseNum(num)
    for digit in parsedNum:
        total += digit
    return total

def main():
    sumOfDigits = getSumDigits(2**1000)
    print "sumOfDigits: %d" % sumOfDigits

if __name__ == "__main__":
    main()
