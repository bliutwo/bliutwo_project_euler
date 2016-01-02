// Filename: pandigitalprime.cpp
// Description: https://projecteuler.net/problem=41

#include <iostream>
#include <iomanip>
#include <locale>
#include <sstream>
#include <string>
#include <vector>
#include "../ConvenientHeaderFiles/printVector.h"
#include <stdio.h>
#include <stdlib.h>

std::vector<std::string> getAllDigits(int digits)
{
	std::vector<std::string> allDigits;
	for (int i = digits; i > 0; i--)
	{
		std::string result;
		std::ostringstream convert;
		convert << i;
		result = convert.str();
		allDigits.push_back(result);
	}
	return allDigits;
}

// TODO: implement this using helper function
//       somehow need to pass in empty string,
//   and somehow need to iteratively pass in 1, 2, 3, and 4
int getRecursivePrime(std::vector<std::string> allDigits)
{
	// recursively pick from left to right
	// check if prime every time you produce a complete number
	// if it is, return that
	
	// once it gets to this point, return -1 since you checked every
	// possible permutation

	return -1;
}

// TODO: implement this
int getLargestPandigitalPrime(int digits)
{
	// start with digits, digits - 1, digits - 2, etc.
	std::vector<std::string> allDigits = getAllDigits(digits);

	// std::cout << std::stoi(allDigits[0]) << std::endl;
	// printVector(allDigits);

	// then switch them such that you go down the list of highest to lowest
	// possible number

	// how do i traverse through the vector such that i go from highest to
	// lowest?
	// recursively pick from left to right
	int prime = getRecursivePrime(allDigits);

	// check if prime every time
	// if it is, return that

	// once it gets to this point, return -1 since you checked every
	// possible permutation
	return prime;
}

int main()
{
	// how to generate a pandigital?
	// how to know at what n to stop? - after x generated "no primes," stop
	int consecutiveLimit = 10;
	int n = 1;
	int consecNoPrimes = 0;
	int panDigitalPrime = getLargestPandigitalPrime(n);
	int digits = n;
	while(consecNoPrimes < consecutiveLimit)
	{
		int nextPanDigPrime = getLargestPandigitalPrime(n+1);
		if (nextPanDigPrime == -1)
		{
			consecNoPrimes++;
		} else {
			panDigitalPrime = nextPanDigPrime;
			digits = n+1;
			consecNoPrimes = 0;
		}
		n++;
	}
	std::cout << "The largest n-digit pandigital prime that exists has ";
	std::cout << digits << " digits and is " << panDigitalPrime;
	std::cout << std::endl;
	return 0;
}
