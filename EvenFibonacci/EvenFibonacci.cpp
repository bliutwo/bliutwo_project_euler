// EvenFibonacci.cpp
// This program generates the sum of all even numbers below a certain number
// in the Fibonacci sequence.

#include<iostream>
#include<vector>

void generateFibo(std::vector<int>&, int);
int sumOfEvens(std::vector<int>&);

int main() {
    int num;
    std::cout << "Enter a number: ";
    std::cin >> num;
    std::vector<int> list;
    generateFibo(list, num);
    int sum = sumOfEvens(list);
    std::cout << "The sum of the even terms of the Fibonacci sequence ";
    std::cout << "below " << num << " is " << sum << std::endl;
    return 0;
}

void generateFibo(std::vector<int>& v, int n)
{
    v.push_back(1);
    v.push_back(2);
    while(v[v.size() - 1] < n)
    {
        v.push_back(v[v.size() - 1] + v[v.size() - 2]);
    }
}

int sumOfEvens(std::vector<int>& v)
{
    int sum = 0;
    for (int i = 0; i < v.size(); i++)
    {
        if(v[i] % 2 == 0)
        {
            sum += v[i];
        }
    }
    return sum;
}
