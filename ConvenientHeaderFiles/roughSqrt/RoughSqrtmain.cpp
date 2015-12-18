#include <iostream>
#include "RoughSqrt.h"

int main()
{
    int num;
    std::cout << "Enter a number to find a rough square root of: ";
    std::cin >> num;
    std::cout << "The rough square root of " << num << " is ";
    std::cout << roughSqrt(num) << std::endl;
    return 0;
}
