#ifndef RETURNLARGESTINVECTOR_H
#define RETURNLARGESTINVECTOR_H

#include <vector>
#include <iostream>

template <class T>
inline T returnLargestInVector(std::vector<T> v)
{
    // does not accept an empty vector
    if(v.empty())
    {
        throw "ERROR: returnLargestInVector does not accept empty vector\n";
    }
    T largest = v[0];
    for (int i = 1; i < v.size(); i++)
    {
        if (v[i] > largest)
        {
            largest = v[i];
            // ...the last statement of this does??
            std::cout << largest << std::endl;
        }
    }
    // TODO: Why does this not always return the largest, while....
    return largest;
}

#endif
