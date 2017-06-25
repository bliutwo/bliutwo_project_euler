# Filename: largestprodingrid.py
# Description: Returns the largest product in a grid.

# TODO: right algorithm seems ok, but down algorithm is probably off
# TODO: the rest of it, mainly diagonal

import sys
import argparse
from chemoUtils import getGrid
sys.dont_write_bytecode = True

def get_greatest(intList):
    return max(intList)

def get_product(prodList):
    product = 1
    for elem in prodList:
        product = product * elem
    print "in function get_product()"
    print product
    return product

def get_all_right(grid):
    listOfRight = []
    for row in grid:
        lastElemIndex = len(row) - 1
        while (lastElemIndex - 4 > 0):
            print "we've entered the while loop"
            prodList = []
            for i in range(0,3):
                prodList.append(row[lastElemIndex - i])
            product = get_product(prodList)
            listOfRight.append(product)
            lastElemIndex = lastElemIndex - 1
    print "in function get_all_right()"
    print listOfRight
    return listOfRight

def get_all_down(grid):
    allDown = []
    rowLength = len(grid[0])
    colLength = len(grid)
    for col in range(3, colLength - 1):
        for row in range(0, rowLength - 1):
            prodList = []
            for i in range(0,3):
                prodList.append(grid[row][col - i])
            product = get_product(prodList)
            allDown.append(product)
    print "in function get_all_down()"
    print allDown
    return allDown

def get_all_diag(grid):
    allDiag = []
    rowLength = len(grid[0])
    colLength = len(grid)

    print "in function get_all_diag()"
    print allDiag
    return allDiag

def get_largest_multiplicant(grid):
    allDown  = get_all_down(grid)
    print allDown
    allRight = get_all_right(grid)
    print allRight
    allDiag  = get_all_diag(grid)
    print allDiag
    allProds = allDown + allRight + allDiag
    print allProds
    greatestProduct = get_greatest(allProds)
    return greatestProduct

def print_grid(g):
    for l in g:
        s = ""
        for w in l:
            s = s + w + " "
        print s

def main():
    parser = argparse.ArgumentParser(description='Returns the largest product in a grid.')
    parser.add_argument("grid", help = "enter the filepath of a grid data file")
    args = parser.parse_args()

    gridfile = open(args.grid)
    grid = getGrid(gridfile)

    print_grid(grid)

    gridfile.close()

    largestMultiplicant = get_largest_multiplicant(grid)
    
    print("largest multiplicant is: %d" % largestMultiplicant)

if __name__ == "__main__":
    main()
