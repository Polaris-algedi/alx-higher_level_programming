#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    sm = 0
    if argc in range(1, 3):
        print("{}".format(0 if argc == 1 else int(sys.argv[1])))
    else:
        for arg in sys.argv[1:]:
            sm += int(arg)
        print("{}".format(sm))
