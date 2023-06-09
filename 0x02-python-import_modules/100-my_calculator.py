#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if not len(argv) == 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

ops = ["+", "-", "*", "/"]
op = argv[2]
a = int(argv[1])
b = int(argv[3])

if op not in ops:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
    
"""Assuming that all arguments will be castable into integers"""
if op == ops[0]:
    print("{} {} {} = {}".format(a, op, b, add(a, b)))
elif op == ops[1]:
    print("{} {} {} = {}".format(a, op, b, sub(a, b)))
elif op == ops[2]:
    print("{} {} {} = {}".format(a, op, b, mul(a, b)))
elif op == ops[3]:
    print("{} {} {} = {}".format(a, op, b, div(a, b)))
