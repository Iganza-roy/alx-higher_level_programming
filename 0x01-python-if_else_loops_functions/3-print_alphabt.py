#!/usr/bin/python3
pr_exc = {'q', 'e'}
for k in range(ord('a'), ord('z') + 1):
    c = chr(k)
    if c not in pr_exc:
        print("{}".format(c), end="")
