#include<iostream>
#include<cmath>

int findSumOfSquares(int);
int findSquareOfSum(int);

int main()
{
    int sumOfSquares;
    int squareOfSum;
    int input;
    std::cout << "Enter a number: ";
    std::cin >> input;
    sumOfSquares = findSumOfSquares(input);
    squareOfSum  = findSquareOfSum(input);
    std::cout << "The difference between the sum of squares of the first ";
    std::cout << input << " numbers and the square of the sum is ";
    std::cout << std::abs(sumOfSquares - squareOfSum) << std::endl;
    return 0;
}

int findSumOfSquares(int limit)
{
    int output = 0;
    for (int i = 0; i <= limit; i++)
    {
        output += (i*i);
    }
    return output;
}

int findSquareOfSum(int limit)
{
    int sum = 0;
    for (int i = 0; i <= limit; i++)
    {
        sum+=i;
    }
    return (sum*sum);
}
