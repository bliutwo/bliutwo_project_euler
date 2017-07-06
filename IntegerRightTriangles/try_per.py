# Filename: try_per.py
# Description: tries different right angle side lengths for triangle

import sys
sys.dont_write_bytecode = True

def try_per(p):
#    print p
    l = []

    for a in range(1, p):
        for b in range(1, p):
            c = p - a - b
            if c**2 == a**2 + b**2:
                d = [a, b, c]
                d.sort()
                if (d not in l):
                    l.append(d)
#    print l
#    print len(l)
    return len(l)


def main():
    print try_per(840)

if __name__ == "__main__":
    main()
