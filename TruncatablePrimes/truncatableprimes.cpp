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
