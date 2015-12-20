# Filename: AmicableNumbers.py
# Description: https://projecteuler.net/problem=21
# Evaluates the sum of all the amicable numbers under 10000.
# See main for definition of amicable number.

# TODO: why doesn't this output the correct answer?

def printList(samplelist):
    samplestring = ",".join(map(str,samplelist))
    print "[%s]" % samplestring

def sumOfElements(listOfInts):
    total = 0
    for integer in listOfInts:
        total += integer
    return total

def getProperDivisors(num):
    listOfProperDivisors = []
    for potentialDivisor in range(1, (num/2)+1):
        if num % potentialDivisor == 0:
            listOfProperDivisors.append(potentialDivisor)
    return listOfProperDivisors

def sumOfProperDivisors(num):
    listOfProperDivisors = getProperDivisors(num)
    return sumOfElements(listOfProperDivisors)

def getAllAmicableNumbers(upperBound):
    setOfAmicableNumbers = set()
    for potentialAmicable in range(1, upperBound):
        if potentialAmicable not in setOfAmicableNumbers:
            secondPotentialAmicable = sumOfProperDivisors(potentialAmicable)
            sumSecondDivisors = sumOfProperDivisors(secondPotentialAmicable)
            if (sumSecondDivisors is potentialAmicable) and (secondPotentialAmicable is not potentialAmicable):
                setOfAmicableNumbers.add(potentialAmicable)
                setOfAmicableNumbers.add(secondPotentialAmicable)
                print "amicable1: %d" % potentialAmicable
                printList(getProperDivisors(potentialAmicable))
                print "amicable2: %d" % secondPotentialAmicable
                printList(getProperDivisors(potentialAmicable))
    return setOfAmicableNumbers

def main():
    # for two numbers a and b to be amicable,
    # d(a) = b and d(b) = a, where d(n) is the sum of proper divisors of n
    # and a != b
    # both a and b are amicable numbers
    upperBound = input("Input an upper bound to compute sum of all amicable numbers: ")
    print "upperBound: %d" % upperBound
    setOfAmicableNumbers = getAllAmicableNumbers(upperBound)
    print "The sum of all the amicable numbers under %d is %d" % (upperBound, sumOfElements(setOfAmicableNumbers))

if __name__ == "__main__":
    main()
