#include <iostream>
#include "../ConvenientHeaderFiles/returnVectorOfPrimes.h"
#include <vector>
#include <fstream>

// TODO: figure out a faster way to solve this problem
//       has to do with divisor function and this link:
//       http://stackoverflow.com/questions/110344/algorithm-to-calculate-the-number-of-divisors-of-a-given-number

int generateTriangleNum(int numTerms)
{
    int sum = 0;
    for (int i = 1; i < (numTerms+1); i++) {
        sum+=i;
    }
    return sum;
}

int getNumDivisors(int triangleNum)
{
    int numDivisors = 0;
    int halfway = triangleNum / 2;
    for (int i = 1; i < (halfway + 1); i++)
    {
        if ((triangleNum % i) == 0)
        {
            numDivisors++;
        }
    }
    return numDivisors;
}

int main(int argc, char* argv[])
{
    int i = 1;
    while(true)
    {
        int triangleNum = generateTriangleNum(i);
        std::cout << "triangleNum: " << triangleNum << std::endl;
        int numDivisors = getNumDivisors(triangleNum);
        std::cout << "numDivisors: " << numDivisors << std::endl;
        if(numDivisors > 500)
        {
            std::cout << "The first triangle number to have over 500 divisors ";
            std::cout << "is: " << triangleNum << std::endl;
            std::ofstream myfile ("solution.txt");
            if (myfile.is_open())
            {
                myfile << "The first triangle number to have over 500 divisors is ";
                myfile << triangleNum;
                myfile.close();
            }
            else std::cout << "Unable to open file\n";
            break;
        }
        std::cout << std::endl;
        i++;
    }
    return 0;
}
