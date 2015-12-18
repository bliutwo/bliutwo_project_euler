#include <iostream>
#include <cmath>

int generatePythProd(int);
bool isPythagorean(int, int);

int main()
{
    int input;
    std::cout << "Enter a number: ";
    std::cin >> input;
    int prod = generatePythProd(input);
    if(prod != -1) std::cout << "The product is: " << prod << std::endl;
    else std::cout << "Product was not found." << std::endl;
    return 0;
}

int generatePythProd(int sum)
{
    // iterate through every possible pythagorean combination of a, b, and c
    // for each combination
    // if (a + b + c) == sum
    // return (a*b*c) 
    for (int a = 1; a < (sum - 1); a++)
    {
        for (int b = 1; b < (sum - 1); b++)
        {
            // std::cout << "Testing " << a << " and " << b << std::endl;
            if(isPythagorean(a, b))
            {
                int c = sqrt(pow(a, 2.0) + pow(b, 2.0));
                // std::cout << "c is: " <<  c << std::endl;
                if ((a + b + c) == sum)
                {
                    std::cout << "Successful sum, " << a << " + " << b;
                    std::cout << " + " << c << " = " << (a + b + c);
                    std::cout << std::endl;
                    return (a * b * c);
                }
            }
        }
    }
    return -1;
}

bool isPythagorean(int a, int b)
{
    double c = sqrt(pow(a, 2.0) + pow(b, 2.0));
    double d = (int)c;
    // std::cout << "c: " << c << "; d: " << d << std::endl;
    // std::cout << "c - d = " << (c-d) << std::endl;
    double zero = 0.0;
    if((c - d) == zero)
    {
        return true;
    }
    else
    {
        return false;
    }
}
