// Multiples3and5.cpp
// This program takes a non-negative, non-zero integer (assuming correct input)
// and returns the sum of all integers below the inputted integer that are
// multiples of 3 and 5.

#include<iostream>
#include<vector>
#include<string>

int sumOfMultiples(int, std::vector<int>&);
void printVector(std::vector<int>&);

int main()
{
    int num;
    std::vector<int> list;

    std::cout << "Enter a number: ";
    std::cin >> num;

    int sum = sumOfMultiples(num, list);
    
    std::cout << std::endl;
    std::cout << "You entered: " << num << std::endl;
    std::cout << "The sum of all the multiples of 3 or 5 below " << num;
    std::cout << " is " << sum << std::endl;

    // printVector(list);
    // std::cout << list.size() << std::endl;
    std::cout << std::endl << "End of program." << std::endl;

    return 0;
}

int sumOfMultiples(int num, std::vector<int>& v)
{
    for (int i = 1; i < num; i++)
    {
        // if this number is a multiple of 3 or 5, add it to the vector
        if((i % 3) == 0 || (i % 5) == 0)
        {
            v.push_back(i);
        }
    }
    int sum = 0;
    for (int i = 0; i < v.size(); i++)
    {
        sum += v[i];
    }
    return sum;
}

void printVector(std::vector<int>& v)
{
    std::cout << "{";
    for (int i = 0; i < v.size() - 1; i++)
    {
        std::cout << v[i] << ", ";
    }
    std::cout << v[v.size() - 1] << "}" << std::endl;
}
