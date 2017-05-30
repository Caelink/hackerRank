#!/bin/python

import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

left_diag = 0
right_diag = 0
for i, x in enumerate(a):
    left_diag += a[i][i]
    right_diag += a[i][n - i - 1]
    
diff = abs(left_diag - right_diag)

print diff
