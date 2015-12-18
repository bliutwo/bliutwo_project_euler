#include <iostream>
#include "../ConvenientHeaderFiles/sumOfVector.h"
#include "../ConvenientHeaderFiles/returnVectorOfPrimes.h"
#include "../ConvenientHeaderFiles/printVector.h"
#include "../ConvenientHeaderFiles/largeSumOfIntVector.h"
#include <vector>
#include <math.h>

// TODO: How to store and perform operations on extremely large numbers? 
//       Specifically, square root of large number? - CHECK, taken care of
//       Store a large sum? - CHECK, long long

// long long int sumOfPrimes(int);

int main()
{
    int input;
    std::cout << "Enter a number: ";
    std::cin >> input;
    // std::cout << "sqrt(" << input << ") = " << sqrt(input) << std::endl;
    std::vector<int> listOfPrimes = returnVectorOfPrimes(input);
    printVector(listOfPrimes);
    std::cout << "The sum of all the primes below " << input << " is ";
    // std::cout << sumOfPrimes(input) << std::endl;
    std::cout << largeSumOfIntVector(listOfPrimes) << std::endl;
    // std::vector <int> v = returnVectorOfPrimes(input);
    return 0;
}

/*
long long int sumOfPrimes(int n)
{
    std::vector<int> listOfPrimes = returnVectorOfPrimes(n);
    return largeSumOfIntVector(listOfPrimes);
}
*/
