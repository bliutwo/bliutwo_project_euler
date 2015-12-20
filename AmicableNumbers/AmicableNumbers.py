# Filename: AmicableNumbers.py
# Description: https://projecteuler.net/problem=21
# Evaluates the sum of all the amicable numbers under 10000.
# See main for definition of amicable number.

# TODO: why doesn't this output the correct answer?

def sumOfElements(listOfInts):
    total = 0
    for integer in listOfInts:
        total += integer
    return total

def sumOfProperDivisors(num):
    listOfProperDivisors = []
    for potentialDivisor in range(1, (num/2)+1):
        if num % potentialDivisor == 0:
            listOfProperDivisors.append(potentialDivisor)
    return sumOfElements(listOfProperDivisors)

def getAllAmicableNumbers(upperBound):
    setOfAmicableNumbers = set()
    for potentialAmicable in range(1, upperBound):
        if potentialAmicable not in setOfAmicableNumbers:
            secondPotentialAmicable = sumOfProperDivisors(potentialAmicable)
            sumSecondDivisors = sumOfProperDivisors(secondPotentialAmicable)
            if sumSecondDivisors is potentialAmicable:
                setOfAmicableNumbers.add(potentialAmicable)
                setOfAmicableNumbers.add(secondPotentialAmicable)
                # print "amicable1: %d" % potentialAmicable
                # print "amicable2: %d" % secondPotentialAmicable
    return setOfAmicableNumbers

def main():
    # for two numbers a and b to be amicable,
    # d(a) = b and d(b) = a, where d(n) is the sum of proper divisors of n
    # both a and b are amicable numbers
    upperBound = input("Input an upper bound to compute sum of all amicable numbers: ")
    setOfAmicableNumbers = getAllAmicableNumbers(upperBound)
    total = 0
    for n in setOfAmicableNumbers:
        # print "n: %d" % n
        total += n
    print "The sum of all the amicable numbers under %d is %d" % (upperBound, total)

if __name__ == "__main__":
    main()
