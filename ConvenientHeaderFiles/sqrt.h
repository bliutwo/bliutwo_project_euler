#ifndef SQRT_H
#define SQRT_H

#include<cmath>

double test(double, double);
bool closeEnough(double, double);
double betterGuess(double, double);

inline double Sqrt(double x)
{
    return test(x,1);
}

double test(double x, double g)
{
    if (closeEnough(x/g, g))
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

#endif
