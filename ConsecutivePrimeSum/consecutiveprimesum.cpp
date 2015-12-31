// Filename: consecutiveprimesum.cpp
// Description: https://projecteuler.net/problem=50

#include <iostream>
#include <vector>
#include "../ConvenientHeaderFiles/returnVectorOfPrimes.h"
#include "../ConvenientHeaderFiles/printVector.h"
#include "../ConvenientHeaderFiles/largeSumOfIntVector.h"
#include "../ConvenientHeaderFiles/isPrime.h"

int longestConsecSeqSumBelowMillion(std::vector<int> listOfPrimes, int limit)
{
    int lengthOfSequence = 0;
    int total = 0;
    for (int i = 0; i < listOfPrimes.size(); i++)
    {
        total += listOfPrimes[i];
        if (total > limit)
        {
            break;
        } else {
            lengthOfSequence++;
        }
    }
    return lengthOfSequence;
}

int calculatePrimeSumMostConsec(int upperBound, std::vector<int> &listOfPrimes,
                                int limit)
{
    int sum = 0;
    int index = 0;
    // calculate initial sum
    for (int i = 0; i < upperBound; i++)
    {
        sum += listOfPrimes[i];
    }
    // change window and calculate sum until greater than limit
    while(sum < limit)
    {
        if(isPrime(sum))
        {
            std::cout << "(" << upperBound << " terms) ";
            return sum;
        } else {
            // subtract element at index i
            // add element at index + upperBound -1 <-- check latter value
            sum -= listOfPrimes[index];
            sum += listOfPrimes[upperBound+index];
            index++;
        }
    }
    return calculatePrimeSumMostConsec(upperBound-1, listOfPrimes, limit);
}

int main(int argc, char* argv[])
{
    int limit;
    std::cout << "Input a num: ";
    std::cin >> limit;
    std::vector<int> listOfPrimes = returnVectorOfPrimes(limit);
    int upperBound = longestConsecSeqSumBelowMillion(listOfPrimes, limit);
    std::cout << "upperBound on length of sequence: " << upperBound << std::endl;
    std::cout << "The prime below " << limit << " that can be written as the ";
    std::cout << std::endl;
    std::cout << "sum of the most consecutive primes: ";
    std::cout << calculatePrimeSumMostConsec(upperBound, listOfPrimes, limit);
    std::cout << std::endl;
    // std::vector<int> listOfPrimeConsecSums = returnPrimeConsecSums(listOfPrimes);
    return 0;
}
