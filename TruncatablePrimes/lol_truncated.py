# Filename: lol_truncated.py
# Description: return a list of all truncations

import sys
sys.dont_write_bytecode = True


def truncated(p):
    l = []
    l.append(str(p))
    s = str(p)
#    print l
    while len(s) > 1:
        l.append(s[1:])
        s = s[1:]
#        print l
    s = str(p)
    while len(s) > 1:
        l.append(s[0:len(s)-1])
        s = s[0:len(s)-1]
#        print l
    il = []
    for s in l:
        il.append(int(s))
    return il

def main():
    print truncated(3797)

if __name__ == "__main__":
    main()
