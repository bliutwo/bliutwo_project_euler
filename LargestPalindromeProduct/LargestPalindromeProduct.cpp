#include<iostream>
#include<string>
#include<vector>

bool isPalindrome(int, int);
std::string reverseString(std::string);
int returnBiggestElement(std::vector<int>);

int main()
{
    std::vector<int> v;
    for (int i = 999; i > 100; i--)
    {
        for (int j = 999; j > 100; j--)
        {
            if(isPalindrome(i, j))
            {
                v.push_back(i * j);
            }
        }
    }
    std::cout << "The largest palindrome made from the product of two ";
    std::cout << "3-digit numbers is: " << returnBiggestElement(v);
    std::cout << std::endl;
    return 0;
}

int returnBiggestElement(std::vector<int> v)
{
    int largest = 0;
    for (int i = 0; i < v.size() - 1; i++)
    {
        if(v[i] > largest)
        {
            largest = v[i];
        }
    }
    return largest;
}


bool isPalindrome(int a, int b)
{
    int num = a * b;
    // std::cout << a << std::endl;
    // std::cout << b << std::endl;
    std::string numero = std::to_string(num);
    std::string backwa = reverseString(numero);
    // std::cout << numero << std::endl;
    // std::cout << backwa << std::endl;
    if(numero == backwa)
    {
        return true;
    } else
    {
        return false;
    }
}

std::string reverseString(std::string a)
{
    std::string b = "";
    for (int i = a.length() - 1; i >= 0; i--)
    {
        b.push_back(a[i]);
    }
    return b;
}
