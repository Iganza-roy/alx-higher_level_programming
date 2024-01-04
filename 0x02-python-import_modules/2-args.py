#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argcnt = len(sys.argv) - 1
    if argcnt == 0:
        print("0 arguments.")
    elif argcnt == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argcnt))
    for i in argcnt:
        print("{}: {}".format(i + 1, sys.arg[i + 1]))
