// Filename: substringdivisibility.cpp
// Description: https://projecteuler.net/problem=43

#include <iostream>
#include <vector>
#include <string>
#include "../ConvenientHeaderFiles/largeSumOfIntVector.h"

// check if each pandigital number has the property listed in the link
std::vector<int> getRelevantPandigitals()
{
	std::vector <int> relevantPandigitals;
	// get all strings where d2 d3 d4 (always refer to product) divis by 2
	// using those strings, get all strings where d3 d4 d5 divis by 3
	// using those strings, get all strings where d4 d5 d6 divis by 5
	// using those strings, get all strings where d5 d6 d7 divis by 7
	// """""""""""""""""""""""""""""""""""""""""""d6 d7 d8 divis by 11
	// 											  d7 d8 d9 divis by 13
	// 											  d8 d9 d10      by 17
	return relevantPandigitals;
}

int main(int argc, char* argv[])
{
	// get relevant pandigital numbers
	std::vector<int> listOfPandigitals = getRelevantPandigitals();
	// get sum of elements in vector
	std::cout << largeSumOfIntVector(listOfPandigitals) << std::endl;
	return 0;
}
