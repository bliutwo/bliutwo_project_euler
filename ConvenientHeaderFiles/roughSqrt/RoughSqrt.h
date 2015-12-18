#ifndef ROUGHSQRT_H
#define ROUGHSQRT_H

#include<string>

inline int roughSqrt(int input)
{
    // calculate what a would be in sqrt(a) * 10^n
    // calculate what a would be in sqrt(a) * 10^n
    // if a < 10, first = 2
    // if a >= 10, first = 6
    // n = (length of string - 1)/2;
    // return first * (10^n);
    
    std::string inpu = std::to_string(input);
    std::string init = "";
    init.push_back(inpu[0]);
    int a = std::stoi(init);
    int first;
    if(a < 10) first = 2;
    else first = 6;

    int n = (inpu.length() - 1)/2;

    return first * (10^n);
}

#endif
