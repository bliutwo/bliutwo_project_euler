#include<iostream>

bool tryDividing(int);

int main()
{
    int num;
    int max = 999999999;
    for (num = 1; num < max; num++)
    {
        if(tryDividing(num*20))
        {
            std::cout << num*20 << " is the smallest positive number that is ";
            std::cout << "evenly divisible by all of the numbers from 1 to ";
            std::cout << "20." << std::endl;
            return 0;
        }
    }
    std::cout << max << " was too small of a cap." << std::endl;
    return 0;
}

bool tryDividing(int n)
{
    for (int i = 1; i <= 20; i++)
    {
        // std::cout << n << " % " << i << " = " << (n%i) << std::endl;
        if((n % i) != 0)
        {
            // std::cout << i << std::endl;
            // std::cout << n << " % " << i << " = " << (n%i) << std::endl;
            return false;
        }
    }
    // std::cout << "finally: " << n << " % 20 = " << (n%20) << std::endl;
    return true;
}
