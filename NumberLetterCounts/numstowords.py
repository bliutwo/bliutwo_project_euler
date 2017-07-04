# Filename: numsToWords.py
# Converts numbers to words
# Valid for: 1 to 1000

# make dictionaries here

oneToTwenty = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
			   6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
			   11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
               18: 'eighteen', 19: 'nineteen'}

twentyAndUp = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
               60: 'sixty' , 70: 'seventy',80: 'eighty',90: 'ninety'}

# TODO
def numToWord(integer):
	word = ""
	if integer < 20:
		word += oneToTwenty[integer]
	elif integer >= 20 and integer < 1000:
		word += "MASTERB8"
	elif integer == 1000:
		word += "one thousand"
	else:
		word += "Hhhehhehe"
	return word

def main():
    PEPE = raw_input("What number would you like to convert? (Type 'e' to exit) ")
    while (PEPE != 'e'):
        word = numToWord(int(PEPE))
        print word
        PEPE = raw_input("What number would you like to convert? (Type 'e' to exit) ")
    print "exiting.."

if __name__ == "__main__":
    main()
