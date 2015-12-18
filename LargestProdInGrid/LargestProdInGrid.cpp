#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "../ConvenientHeaderFiles/returnLargestInVector.h"
#include "../ConvenientHeaderFiles/splitString.h"
#include "../ConvenientHeaderFiles/printVector.h"

std::vector<std::vector<int>> parseGrid(char*);
std::vector<long long int> getAllAdjacentProds(const std::vector<std::vector<int>> grid);
std::vector<int> parseListOfInts(std::string line);
void printGrid(std::vector<std::vector<int>>);
int getDiagProd(std::vector<std::vector<int>> grid, int row, int col);
int getRightProd(std::vector<std::vector<int>> grid, int row, int col);
int getDownProd(std::vector<std::vector<int>> grid, int row, int col);

int main(int argc, char* argv[])
{
    // accept the data file from the command line
    // if the number of arguments is improper, tell the user that
    if (argc != 2) {
        std::cout << "You need to specify a data file." << std::endl;
        std::cout << "usage: ./LargestProdInGrid [data.txt]" << std::endl;
        return 0;
    }
    // read in the file
    std::vector<std::vector<int>> grid = parseGrid(argv[1]);
    // printGrid(grid);
    if(!grid.empty()) {
        // get a vector of the products of all possible adjacent numbers
        //     up, down, left, right, or diagonally
        std::vector<long long int> listOfProducts = getAllAdjacentProds(grid);
        std::cout << "Successfully read." << std::endl;
        // return the largest product in the vector
        long long int largest = returnLargestInVector(listOfProducts);
        std::cout << "Largest \"adjacent product\" in grid: " << largest;
        std::cout << std::endl;
    } else {
        std::cout << "Unable to parse grid." << std::endl;
    }
    return 0;
}

std::vector<std::vector<int>> parseGrid(char* filename)
{
    // std::cout << "Filename: " << filename << std::endl;
    std::vector<std::vector<int>> grid;
    // lines are rows, inside vector
    std::ifstream fileObj;
    fileObj.open(filename, std::ios::in);
    std::string line;
    if(fileObj.is_open()) {
        while(std::getline(fileObj,line))
        {
            std::vector<int> listOfInts = parseListOfInts(line);
            // add vector to grid
            grid.push_back(listOfInts);
        }
    }
    // else it's an empty grid
    return grid;
}

std::vector<int> parseListOfInts(std::string line)
{
    // declare a vector of ints
    std::vector<int> listOfInts;
    // get a vector of split strings
    std::vector<std::string> listOfStringInts = split(line, ' ');
    for (int i = 0; i < listOfStringInts.size(); i++)
    {
        // convert each string to an int, then add to listOfInts
        listOfInts.push_back(std::stoi(listOfStringInts[i]));
    }
    return listOfInts;
}

std::vector<long long int> getAllAdjacentProds(const std::vector<std::vector<int>> grid)
{
    std::vector<long long int> allAdjacentProds;
    // for each number, get all possible adjacent products
    for (int row = 0; row < grid.size(); row++)
    {
        for (int col = 0; col < (grid[row]).size(); col++)
        {
            // do your work here on each number
            // down
            int down = getDownProd(grid, row, col);
            // right
            int right = getRightProd(grid, row, col);
            // diagonal north-east
            int diagonal = getDiagProd(grid, row, col);
            allAdjacentProds.push_back(down);
            allAdjacentProds.push_back(right);
            allAdjacentProds.push_back(diagonal);
        }
    }
    return allAdjacentProds;
}

int getDownProd(std::vector<std::vector<int>> grid, int row, int col)
{

    return 0;
}

int getRightProd(std::vector<std::vector<int>> grid, int row, int col)
{

    return 0;
}

int getDiagProd(std::vector<std::vector<int>> grid, int row, int col)
{

    return 0;
}

void printGrid(std::vector<std::vector<int>> grid)
{
    for (int i = 0; i < grid.size(); i++)
    {
        printVector(grid[i]);
    }
}
