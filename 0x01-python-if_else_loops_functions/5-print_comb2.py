#!/usr/bin/python3
for nbr in range(100):
    if (nbr == 99):
        print("{0:02d}".format(nbr))
    else:
        print("{0:02d}, ".format(nbr), end="")
