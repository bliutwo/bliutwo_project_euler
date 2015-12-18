// File: LatticePaths.c
// Description: In theory, I only need ints to solve this problem.

#include <stdio.h>

int solvePaths(int num)
{

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
