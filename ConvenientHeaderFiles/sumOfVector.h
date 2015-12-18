#ifndef SUMOFVECTOR_H
#define SUMOFVECTOR_H

#include <vector>

template <class T>
inline T sumOfVector(std::vector<T> v)
{
    // does not accept an empty vector
    if(v.empty())
    {
        throw "ERROR: sumOfVector does not accept empty vector\n";
    }
    T sum = v[0] * 0.0;
    for (int i = 0; i < v.size(); i++)
    {
        sum += v[i];
    }
    return sum;
}

#endif
