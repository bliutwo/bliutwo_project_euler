#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "../ConvenientHeaderFiles/printVector.h"

// TODO: figure out how to store a 50-digit number

std::vector<unsigned long long int> getListOfNums(const char*);

int main(int argc, char* argv[])
{
    if (argc != 2) {
        std::cout << "You need to specify a data file." << std::endl;
        std::cout << "usage: ./LargeSum [data.txt]" << std::endl;
        return 0;
    }
    std::vector<unsigned long long int> listOfNums = getListOfNums(argv[1]);
    printVector(listOfNums);
    return 0;
}

std::vector<unsigned long long int> getListOfNums(const char* filename)
{
    std::vector<unsigned long long int> listOfNums;
    std::string line;
    std::ifstream fileObj(filename);
    if (fileObj.is_open())
    {
        while(std::getline(fileObj, line))
        {
            // get a number out of every line
            unsigned long long int num = std::stoull(line);
            // add num to list
            listOfNums.push_back(num);
        }
    }
    return listOfNums;
}
