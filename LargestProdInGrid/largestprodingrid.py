# Filename: largestprodingrid.py
# Description: Returns the largest product in a grid.

# TODO: right algorithm ok
# TODO: check accuracy of down
# TODO: convert grid to downgrid, then use right algorithm
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
#    print "in function get_product()"
#    print prodList
#    print product
    return product

def get_all_right(grid):
    print "in function get_all_right()"
    listOfRight = []
    for row in grid:
#        print row
        lastElemIndex = len(row) - 1
#        print len(row)
#        print lastElemIndex
        while (lastElemIndex - 1 > 0):
#            print "we've entered the while loop"
            prodList = []
            for i in range(0,3):
                prodList.append(row[lastElemIndex - i])
#            print prodList
#            print row
            product = get_product(prodList)
#            print product
            listOfRight.append(product)
            lastElemIndex = lastElemIndex - 1
#    print listOfRight
    return listOfRight

def get_all_diag(grid):
    allDiag = []
    rowLength = len(grid[0])
    colLength = len(grid)

    print "in function get_all_diag()"
    print allDiag
    return allDiag

def make_down_grid(g):
    dg = []
    return dg

def get_largest_multiplicant(grid):
    allRight = get_all_right(grid)
    print allRight
    dg = make_down_grid(grid)
    allDown  = get_all_right(dg)
    print allDown

    assert(False)

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
            s = s + str(w) + " "
        print s

def int_up_grid(sg):
    ig = []
    for r in sg:
        tl = []
        s = r[0]
        lol = s.split()
#        print lol
        for unit in lol:
            n = int(unit)
            tl.append(n)
        ig.append(tl)
#        print ig
    return ig

def main():
    parser = argparse.ArgumentParser(description='Returns the largest product in a grid.')
    parser.add_argument("grid", help = "enter the filepath of a grid data file")
    args = parser.parse_args()

    gridfile = open(args.grid)
    grid = getGrid(gridfile)

    print "Just before print_grid"
    print_grid(grid)

    gridfile.close()

#    print "Just before print_grid2" 
#    print_grid(grid)
    g = int_up_grid(grid)
#    print g
    
    print "PRINT_GRID G"
    print_grid(g)

    largestMultiplicant = get_largest_multiplicant(g)
    
    print("largest multiplicant is: %d" % largestMultiplicant)

if __name__ == "__main__":
    main()
