#!/bin/python

import sys

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(raw_input().strip())

print factorial(n)
