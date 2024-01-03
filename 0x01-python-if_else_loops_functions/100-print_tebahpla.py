#!/usr/bin/python3
for i in range(ord('z'), ord('a') -1, -1):
    if i % 2 == 0:
        res = 0
    else:
        res = 32
    print("{}".format(chr(i - res)), end="")
