#include<iostream>
#include<cmath>

double sqrt(double);
double test(double, double);
bool closeEnough(double, double);
double betterGuess(double, double);

int main()
{
    double num;
    std::cout << "Enter a number: ";
    std::cin >> num;
    std::cout << "The square root of " << num << " is " << sqrt(num);
    std::cout << std::endl;
    return 0;
}

double sqrt(double x)
{
    return test(x, 1);
}

double test(double x, double g)
{
    if closeEnough(x/g, g)
        return g;
    else
        return test(x, betterGuess(x, g));
}

bool closeEnough(double a, double b) {
    return (std::abs(a - b) < 0.00001);
}

double betterGuess(double x, double g) {
    return ((g + x/g) / 2);
}
