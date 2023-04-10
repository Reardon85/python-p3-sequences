#!/usr/bin/env python3

def print_fibonacci(length):
    num1, num2 = 0, 1
    i = 0
    fib = list()
    while (i < length):
        fib.append(num1)
        num1, num2 = num2, num1 + num2
        i += 1
    print(fib)