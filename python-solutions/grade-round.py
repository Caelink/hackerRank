#!/bin/python

import sys

def solve(grades):
    for i, grade in enumerate(grades):
        if (grade > 37) and ((grade % 5) > 2):
                grades[i] += (5 - (grade % 5))
    return grades

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))