// Filename: truncatableprimes.cpp
// Description: https://projecteuler.net/problem=37

#include <iostream>
#include "../ConvenientHeaderFiles/isPrime.h"
#include "../ConvenientHeaderFiles/printVector.h"
#include "../ConvenientHeaderFiles/sumOfVector.h"
#include <vector>

// most of this info from i3wm_rules_ok from twitch chat

// algorithm: get primes, add another prime to the prime (on each side),
// then check if the resulting number is prime
// apparently the starting digits are 3 or 7
// truncatable primes can only end in 3 or 7
// further, 2 or 5 can only occur at most once in the prime, and only
// in the beginning
// and only the digits 1 2 3 5 7 9 can be used to build it up (naturally)

int main(int argc, char* argv[])
{
	std::vector<int> listOfPrimes;
	for (int i = 2; i < 10; i++)
	{
		if (isPrime(i))
		{
			listOfPrimes.push_back(i);
		}
	}
	printVector(listOfPrimes);
	std::cout << "The size of listOfPrimes is " << listOfPrimes.size();
	std::cout << std::endl;
	std::cout << "The sum of the elements in listOfPrimes is ";
	std::cout << sumOfVector(listOfPrimes);
	std::cout << std::endl;
	return 0;
}
