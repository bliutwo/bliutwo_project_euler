# Filename: numsToWords.py # Converts numbers to words
# Valid for: 1 to 1000

# make dictionaries here

oneToTwenty = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
			   6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
			   11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
               18: 'eighteen', 19: 'nineteen', 0: ''}

twentyAndUp = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
               60: 'sixty' , 70: 'seventy',80: 'eighty',90: 'ninety'}

hundredThousand = {4: 'thousand', 3: 'hundred'}

# TODO
# recursively add stuff
def numToWord(int_str):
    integer = int(int_str)
    if integer < 20:
        return oneToTwenty[integer]
    elif len(int_str) == 2:
        if int_str[-1] == '0':
            return twentyAndUp[integer]
        else:
            new_str = int_str[0] + '0'
            return twentyAndUp[int(new_str)] + numToWord(int_str[1:])
    else:
        s = oneToTwenty[int(int_str[0])] + hundredThousand[len(int_str)]
        t = numToWord(int_str[1:])
        if t == "":
            return s
        else:
            s = s + "and" + t
            return s

def main():
    PEPE = raw_input("What number would you like to convert? (Type 'e' to exit) ")
    while (PEPE != 'e'):
        word = numToWord(PEPE)
        print "%s\t%d" % (word, len(word))
        PEPE = raw_input("What number would you like to convert? (Type 'e' to exit) ")
    print "exiting.."

if __name__ == "__main__":
    main()
