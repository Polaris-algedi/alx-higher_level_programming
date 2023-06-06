#!/usr/bin/python3
start_char = ord('a')
end_char = ord('z')

for char_code in range(start_char, end_char + 1):
    print("{}".format(chr(char_code)), end="")
