#include<iostream>
#include<vector>
#include<math.h>
#include "printVector.h"
#include "isPrime.h"

int findPrime(int);
int returnNextPrime(std::vector<int>);
bool isPrime(int);

int main()
{
    int input;
    std::cout << "Which number prime number do you wish to find? ";
    std::cin >> input;
    int output = findPrime(input);
    std::cout << "Prime number #" << input << ": " << output << std::endl;
    return 0;
}

int findPrime(int num)
{
    std::vector<int> listOfPrimes;
    while (listOfPrimes.size() < num)
    {
        listOfPrimes.push_back(returnNextPrime(listOfPrimes));
    }
    printVector(listOfPrimes);
    return listOfPrimes[listOfPrimes.size() - 1];
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

// does not accept 1 or <= 0
/*
bool isPrime(int x)
{
    if (x <= 0)
    {
        throw "isPrime does not accept x <= 0";
    }
    else if (x == 1)
    {
        throw "isPrime does not accept 1";
    }
    else if (x == 2)
    {
        return true;
    }
    else if (((x%2) == 0) && (x>3))
    {
        return false;
    }
    else
    {
        for (int i = 3; i < (sqrt(x) + 1); i+=2)
        {
            if((x%i)==0) return false;
        }
        return true;
    }
}
*/
