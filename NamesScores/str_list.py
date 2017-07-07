# Filename: str_list.py
# Description: return a list of strings from file

import sys
sys.dont_write_bytecode = True

from alphanumdict import alphanumdict

def get_alphanum_value(s, d):
    t = 0
    for c in s:
        if c in d:
            t += d[c]
    return t

def get_file_str_list(fname):
    l = []
    # https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
    with open(fname) as f:
        l = f.readlines()
    print len(l)
    # you may also want to remove whitespace characters
    # like '\n' at the end of each line
    s = l[0]
# https://stackoverflow.com/questions/12088442/python-how-to-separate-string-with-comma
    li = s.strip().split(",")
    return li

def main():
    l = get_file_str_list("p022_names.txt")
    d = alphanumdict()
    values = []
    for s in l:
        v = get_alphanum_value(s, d)
        values.append((s, v))
    print values


if __name__ == "__main__":
    main()
