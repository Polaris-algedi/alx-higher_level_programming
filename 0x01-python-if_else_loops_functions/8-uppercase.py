#!/usr/bin/python3
def uppercase(str):
    u_str = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            u_str += chr(ord(char) - ord('a') + ord('A'))
        else:
            u_str += char
    print(u_str)
