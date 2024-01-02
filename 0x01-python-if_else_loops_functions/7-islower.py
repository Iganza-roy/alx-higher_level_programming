#!/usr/bin/python3
def islower(c):
    for k in range(ord('a'), ord('z') + 1):
        if c in chr(k):
            return (True)
    return (False)
