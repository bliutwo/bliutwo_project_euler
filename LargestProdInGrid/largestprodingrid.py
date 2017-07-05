# Filename: largestprodingrid.py
# Description: Returns the largest product in a grid.

# TODO: right algorithm ok.. DONE!
# TODO: check accuracy of down.. DONE!
# TODO: convert grid to downgrid, then use right algorithm.. DONE!
# TODO: the rest of it, mainly diagonal

import sys
sys.dont_write_bytecode = True

import argparse

# returns a grid with all information given an opened file of the csv file
def getGrid(opened):
    # use opened to obtain the list of pairs
    # read first line of file since the first line is a "key/legend"
    # opened.readline()
    grid = []
    for line in opened:
        # parse line to get first part of pair
        line = line.strip()
        lineList = line.split(",")
        grid.append(lineList)
    return grid

def print_grid(g):
    for l in g:
        s = ""
        for w in l:
            s = s + str(w) + " "
        print s

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
        while (lastElemIndex - 2 > 0):
#            print "we've entered the while loop"
            prodList = []
            for i in range(0,4):
                prodList.append(row[lastElemIndex - i])
#            print prodList
#            print row
            product = get_product(prodList)
#            print product
            listOfRight.append(product)
            lastElemIndex = lastElemIndex - 1
#    print listOfRight
    return listOfRight


# TODO
def get_all_diag(grid):
    allDiag = []
    numRows = len(grid)
    numCols = len(grid[0])
    print numRows
    print numCols
    assert(False)
    return allDiag

def make_down_grid(g):
    dg = []
    for i in range(0, len(g[0])):
        col = []
        for row in g:
            col.append(row[i]) 
        dg.append(col)
    return dg

def get_largest_multiplicant(grid):
    allRight = get_all_right(grid)
#    print allRight
    dg = make_down_grid(grid)
#    print_grid(grid)
#    print "About to print dg"
#    print_grid(dg)
    allDown  = get_all_right(dg)
#    print allDown
    allDiag  = get_all_diag(grid)
    print allDiag
    assert(False)
    allProds = allDown + allRight + allDiag
    print allProds
    greatestProduct = get_greatest(allProds)
    return greatestProduct

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
