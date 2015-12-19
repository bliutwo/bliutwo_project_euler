// File: LatticePaths.c
// Description: In theory, I only need ints to solve this problem.

#include <stdio.h>
#include <stdlib.h>

int solvePaths(int num)
{
    // create dynamically allocated grid of (num + 1) * (num + 1)

    // recursively backtrack to get number of routes to bottom right corner
    return 0;
}

int main(int argc, char* argv[])
{
    int num = 0;
    
    printf("Enter an integer: ");
    scanf("%d", &num);

    printf("This is num that you inputted: %d\n", num);

    int paths = solvePaths(num);
    
    printf("Number of routes in a %dx%d grid: %d\n", num, num, paths);

    return 0;
}
