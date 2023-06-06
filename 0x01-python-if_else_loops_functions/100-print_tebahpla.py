#!/usr/bin/python3
a = ord('a')
z = ord('z')
A = ord('A')
for c in range(z, a - 1, -1):
    print("{}".format(chr(c) if c % 2 == 0 else chr(c - a + A)), end="")
