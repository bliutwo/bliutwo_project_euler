#ifndef PRINTVECTOR_H
#define PRINTVECTOR_H

#include<vector>
#include<iostream>

template <class T>
inline void printVector(std::vector<T> &v)
{
    std::cout << "[";
    for (int i = 0; i < v.size(); i++)
    {
        std::cout << v[i];
        if(i != (v.size() - 1))
        {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;
}

#endif
