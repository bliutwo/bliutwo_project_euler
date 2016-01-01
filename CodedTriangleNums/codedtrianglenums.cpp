// Filename: codedtrianglenums.cpp
// Description: https://projecteuler.net/problem=42

#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char* argv[])
{
    // get the string that is in the data file
    if (argc != 2)
    {
        std::cout << "You need to specify a data file." << std::endl;
        std::cout << "usage: ./codetrianglenums [data.txt]" << std::endl;
        return 0;
    }
    std::string line;
    std::ifstream fileObj(argv[1]);
    if (fileObj.is_open())
    {
        std::getline(fileObj, line);
    }
    std::cout << line << std::endl;
    return 0;
}
