#!/usr/bin/python3
def print_last_digit(number):
    l_dt = abs(number) % 10
    print(l_dt, end="")
    return l_dt
