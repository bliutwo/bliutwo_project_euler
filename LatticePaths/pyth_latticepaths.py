# Filename: pyth_latticepaths.py
# Description: python is easier

import sys
sys.dont_write_bytecode = True

def make_grid(s):
    grid = []
    row = []
    for x in range(0, s):
        row.append(0)
    for x in range(0, s):
        grid.append(row)
    return grid

def print_grid(g):
    for r in g:
        s = ""
        for i in r:
            s = s + str(i) + " "
        print s

def solve_paths(g):
    return 0

def main():
    s = input("Enter a number: ")
    g = make_grid(s)
    print_grid(g)
    n = solve_paths(g)
    print "The number of routes through a %d x %d grid is %d." % (s, s, n)

if __name__ == "__main__":
    main()
