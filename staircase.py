#!/bin/python

import sys

n = int(raw_input().strip())

reverse = [(n - x) for x in range(0, n)]

for x in reverse:
    for y in range(0, n):
        if (y+1 < x):
            sys.stdout.write(' ')
        else:
            sys.stdout.write('#')
    sys.stdout.write('\n')
