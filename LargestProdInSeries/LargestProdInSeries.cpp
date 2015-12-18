#include <iostream>
#include "../ConvenientHeaderFiles/returnLargestInVector.h"
#include "../ConvenientHeaderFiles/printVector.h"
#include <vector>
#include <fstream>
#include <string>
#include <assert.h>

// TODO: Figure out why you can't get the right answer.
//       It has to do with returnLargestInVector and its return value.

int returnGreatestProduct(std::string number);

int main()
{
    /*
    std::vector<double> v = {2.3, 4.5, 6.7, 8.4, 4.6, 1.0};
    printVector(v);
    std::cout << returnLargestInVector(v) << std::endl;
    */
    std::string number = "";
    std::string line;
    int product;
    std::ifstream myfile("Number.txt");
    if(myfile.is_open())
    {
        while(getline(myfile, line))
        {
            // do something with line
            // specifically, add line to number
            number.append(line);
        }
        myfile.close();
    }
    else std::cout << "Unable to open file" << std::endl;
    if(!number.empty())
    {
        std::cout << "Success!" << std::endl;
        std::cout << number << std::endl;
        product = returnGreatestProduct(number);
        std::cout << "The value of the greatest product of 13 adjacent ";
        std::cout << "digits is " << product << std::endl;
    }
    return 0;
}

// accepts a string that is a number
// returns the greatest product of 13 adjacent digits
int returnGreatestProduct(std::string number)
{
    std::vector<long long int> listOfProds;
    for (int i = 0; (i + 13) < number.size(); i++)
    {
        std::vector<long long int> componentProd;
        long long int prod = 1;
        for(int j = i; j < (i + 13); j++)
        {
            // std::cout << prod << std:: endl;
            char c = number[j];
            int ic = c - '0';
            long long int icc = (long long int)ic;
            componentProd.push_back(icc);
            prod *= ic;
            // std::cout << c << " " << ic << " " << prod << std::endl;
        }
        // printVector(componentProd);
        // std::cout << prod << std::endl;
        listOfProds.push_back(prod);
    }
    printVector(listOfProds);
    return returnLargestInVector(listOfProds);
}
