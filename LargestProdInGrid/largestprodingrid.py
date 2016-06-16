# Filename: largestprodingrid.py
# Description: Returns the largest product in a grid.

# TODO: right algorithm seems ok, but down algorithm is probably off
# TODO: the rest of it, mainly diagonal

import sys
import argparse
from chemoUtils import getGrid
sys.dont_write_bytecode = True

def getProduct(prodList):
    product = 1
    for elem in prodList:
        product = product * elem
    return product

def getAllRight(grid):
    listOfRight = []
    for row in grid:
        lastElemIndex = len(row) - 1
        while (lastElemIndex - 4 > 0):
            prodList = []
            for i in range(0,3):
                prodList.append(row[lastElemIndex - i])
            product = getProduct(prodList)
            listOfRight.append(product)
            lastElemIndex = lastElemIndex - 1
    return listOfRight

def getAllDown(grid):
    allDown = []
    rowLength = len(grid[0])
    colLength = len(grid)
    for col in range(3, colLength - 1):
        for row in range(0, rowLength - 1):
            prodList = []
            for i in range(0,3):
                prodList.append(grid[row][col - i])
            product = getProduct(prodList)
            allDown.append(product)
    return allDown

def getAllDiag(grid):
    allDiag = []
    rowLength = len(grid[0])
    colLength = len(grid)
    
    return allDiag

def getLargestMultiplicant(grid):
    allDown  = getAllDown(grid)
    allRight = getAllRight(grid)
    allDiag  = getAllDiag(grid)
    allProds = allDown + allRight + allDiag
    greatestProduct = getGreatest(allProds)
    return greatestProduct

def main():
    parser = argparse.ArgumentParser(description='Returns the largest product in a grid.')
    parser.add_argument("grid", help = "enter the filepath of a grid data file")
    args = parser.parse_args()

    gridfile = open(args.grid)
    grid = getGrid(gridfile)

    gridfile.close()

    largestMultiplicant = getLargestMultiplicant(grid)
    
    print("largest multiplicant is: %d" % largestMultiplicant)

if __name__ == "__main__":
    main()
