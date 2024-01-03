#!/usr/bin/python3
for i in range(ord('z'), ord('A') -1, -1):
    print("{:c}{:c}".format(i, i - (ord('a') - ord('A'))), end="")
