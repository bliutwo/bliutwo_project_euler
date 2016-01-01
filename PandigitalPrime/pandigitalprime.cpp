// Filename: pandigitalprime.cpp
// Description: https://projecteuler.net/problem=41

#include <iostream>

// TODO: implement this
int getLargestPandigitalPrime(int digits)
{
	// start with digits, digits - 1, digits - 2, etc.
	// then switch them such that you go down the list of highest to lowest
	// possible number
	// check if prime every time
	return -1;
}

int main()
{
	// how to generate a pandigital?
	// how to know at what n to stop? - after x generated "no primes," stop
	int n = 1;
	int consecNoPrimes = 0;
	int panDigitalPrime = getLargestPandigitalPrime(n);
	int digits = n;
	while(consecNoPrimes < 10)
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
