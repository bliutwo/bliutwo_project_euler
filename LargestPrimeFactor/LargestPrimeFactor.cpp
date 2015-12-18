#include <iostream>
#include <vector>
#include <math.h>
#include "sqrt.h"
#include "FastInvSqrt.h"
// #include <boost/multiprecision/mpfr.hpp>
#include <string>
#include <utility>

std::vector<int> generatePrimeFacts(long int);
// std::vector<int> generatePrimes(int);
bool isPrime(int);
void printVector(std::vector<int>&);
// void boostMultPrecEx();
// std::vector<int> generatePrimeFactsBoost(std::string numString);

int main()
{
    // boostMultPrecEx();
    // std::cout << "End function." << std::endl;
    long int num;
    std::cout << "Enter a number: ";
    std::cin  >> num;
    std::vector<int> primeFactList = generatePrimeFacts(num);
    /*
    std::string numString;
    std::cout << "Enter a number: ";
    std::cin >> numString;
    std::vector<int> primeFactList = generatePrimeFactsBoost(numString);
    */
    std::cout << "The largest prime factor of " << num << " is ";
    std::cout << primeFactList[primeFactList.size() - 1] << std::endl;
    printVector(primeFactList);
    return 0;
}

/*
std::vector<int> generatePrimeFactsBoost(std::string numString)
{
    std::vector<int> primeFacts;
    primeFacts.push_back(1);
    if((n % 2) == 0) primeFacts.push_back(2);
    // convert numString to n
    // replace Sqrt with boostmultiprecision
    for (int i = 3; i < (int)(Sqrt(n)) + 1; i+=2)
    {
        if(isPrime(i))
        {
            // it's prime mothafucka
            // check if it's a factor of n
            if((n % i) == 0)
            {
                primeFacts.push_back(i);
                printVector(primeFacts);
            }
        }
    }
    return primeFacts;

}
*/

std::vector<int> generatePrimeFacts(long int n)
{
    std::vector<int> primeFacts;
    primeFacts.push_back(1);
    // std::cout << "Sqrt(n): " << Sqrt(n) << std::endl;
    std::cout << "sqrt(n): " << sqrt(n) << std::endl;
    std::cout << "(int)(sqrt(n)): " << (int)(sqrt(n)) << std::endl;
    // std::cout << "Q_rsqrt(n): " << Q_rsqrt(n) << std::endl;
    // std::cout << "1/Q_rsqrt(n): " << 1/Q_rsqrt(n) << std:: endl;
    int squareRootMarker = (int)sqrt(n) + 1;
    if((n % 2) == 0) primeFacts.push_back(2);
    for (int i = 3; i < squareRootMarker; i+=2)
    {
        if(isPrime(i))
        {
            // it's prime mothafucka
            // check if it's a factor of n
            if((n % i) == 0)
            {
                primeFacts.push_back(i);
                printVector(primeFacts);
            }
        }
    }
    return primeFacts;
}

// returns whether an integer is prime or not
// n will be odd and at least 3
bool isPrime(int n)
{
    // something recursive and cool should to happen right here right now
    for(int i = 3; i < (int)(sqrt(n)) + 1; i+=2)
    {
        if((n%i)==0) return false;
    }
    return true;
}

/*
std::vector<int> generatePrimes(int n)
{
    std::vector<int> v;
    v.push_back(1);
    if((n % 2) == 0) v.push_back(2);
    for (int i = 3; i < n; i+=2)
    {
        if
    }
    return v;
}
*/

void printVector(std::vector<int> &v)
{
    std::cout << "{";
    for (int i = 0; i < v.size(); i++)
    {
        std::cout << v[i];
        if(i != (v.size() - 1))
        {
            std::cout << ", ";
        }
    }
    std::cout << "}" << std::endl;
}

/*
void boostMultPrecEx()
{
    std::string s(100, '0');
    s.at(0) = '1';
    boost::multiprecision::mpfr_float_100 f(std::move(s));
    boost::multiprecision::mpfr_float_100 sqrt = boost::multiprecision::sqrt(f);
    std::cout << sqrt.str() << std::endl;
}
*/
