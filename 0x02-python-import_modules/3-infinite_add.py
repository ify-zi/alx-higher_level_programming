#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = 1
    n = 1
    res = 0
    while a <= len(argv) - 1:
        res = res + int(argv[n])
        a += 1
        n += 1
    print("{:d}".format(res))
