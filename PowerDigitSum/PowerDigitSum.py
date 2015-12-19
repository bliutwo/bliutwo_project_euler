# File: PowerDigitSum.py
# Description: https://projecteuler.net/problem=16

def parseLong(num):
    parsedLong = []
    number_string = str(num)
    for ch in number_string:
        parsedLong.append(int(ch))
    print type(parsedLong)
    return parsedLong

def main():
    twoToThousand = 2**1000
    total = 0
    parsedTwoToThousand = parseLong(twoToThousand)
    for digit in parsedTwoToThousand:
        total += digit
    print "Total: %d" % total

if __name__ == "__main__":
    main()
