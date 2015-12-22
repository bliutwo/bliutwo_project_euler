// File: LatticePaths.c
// Description: In theory, I only need ints to solve this problem.

#include <stdio.h>
#include <stdlib.h>

// TODO: write this
void printGrid(int grid[num][num])
{
    for (int row = 0; row < num; row++)
    {
        for (int col = 0; col < num; col++)
        {
            // 145237
            // http://www.kbb.com/company/privacy-policy/
        }
    }
}

int solvePaths(int num)
{
    // create dynamically allocated grid of (num + 1) * (num + 1)
    int grid[num][num];
    for (int row = 0; row < num; num++)
    {
        for (int col = 0; col < num; num++)
        {
            grid[row][col] = 0;
        }
    }
    printGrid(grid);
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
