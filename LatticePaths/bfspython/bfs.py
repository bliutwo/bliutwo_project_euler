# Filename: bfs.py
# Description: https://projecteuler.net/problem=15

import sys
sys.dont_write_bytecode = True

import time

# graph is in adjacent list representation
graph = {
        '1': ['2', '4'],
        '2': ['3', '5'],
        '3': ['6'],
        '4': ['5', '7'],
        '5': ['6', '8'],
        '6': ['9'],
        '7': ['8'],
        '8': ['9']
        }

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE

    print bfs(graph, '1', '9')

    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
#    print t
#    fo = open("results.txt", "wb")
#    fo.write("%r\n%.8f\n" % (t, sumtime))
#    fo.close()


if __name__ == "__main__":
    main()
