# Filename: dfs.py
# Description: https://projecteuler.net/problem=15

import sys
sys.dont_write_bytecode = True

import time

num_paths = 0

def get_num_paths(rights_taken, downs_taken, max_rights, max_downs):
    if rights_taken == max_rights and downs_taken == max_downs:
        global num_paths
        num_paths += 1
        return
    # try turning right, if you can
    if rights_taken < max_rights:
        get_num_paths(rights_taken + 1, downs_taken, max_rights, max_downs);
    # try turning down, if you can
    if downs_taken < max_downs:
        get_num_paths(rights_taken, downs_taken + 1, max_rights, max_downs);
    return


def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE

    max_rights = 20
    max_downs  = 20

    rights_taken = 0
    downs_taken  = 0

    get_num_paths(rights_taken, downs_taken, max_rights, max_downs)

    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
    t = num_paths
    print t
    fo = open("results.txt", "wb")
    fo.write("%r\n%.8f\n" % (t, sumtime))
    fo.close()


if __name__ == "__main__":
    main()
