#ifndef LARGESUMOFINTVECTOR_H
#define LARGESUMOFINTVECTOR_H

#include <vector>

inline long long int largeSumOfIntVector(std::vector<int> v)
{
    // does not accept an empty vector
    if(v.empty())
    {
        throw "ERROR: largeSumOfVector does not accept empty vector\n";
    }
    long long int sum = 0;
    for (int i = 0; i < v.size(); i++)
    {
        sum += (long long int)v[i];
    }
    return sum;
}

#endif
