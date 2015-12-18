#ifndef RETURNVECTOROFPRIMES_H
#define RETURNVECTOROFPRIMES_H

#include <vector>
#include "isPrime.h"

int returnNextPrime(std::vector<int> v);

// returns vector of primes less than limit
inline std::vector<int> returnVectorOfPrimes(int limit)
{
    std::vector<int> listOfPrimes;
    while (listOfPrimes.empty() || (returnNextPrime(listOfPrimes) < limit))
    {
        listOfPrimes.push_back(returnNextPrime(listOfPrimes));
    }
    return listOfPrimes;
}

int returnNextPrime(std::vector<int> v)
{
    if(v.empty())
    {
        return 2;
    }
    else
    {
        int curr = v[v.size() - 1];
        curr++;
        while(!isPrime(curr))
        {
            curr++;
        }
        return curr;
    }
}

#endif
