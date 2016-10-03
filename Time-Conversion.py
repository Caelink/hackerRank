#!/bin/python

import sys


time = raw_input().strip().split(':')
ispm = time[2][2:] == 'PM'
hours = int(time[0])
mins = int(time[1])
secs = int(time[2][:2])

if hours == 12:
    hours -= 12

if ispm:
    hours += 12

print '%02d:%02d:%02d'%(hours,mins,secs)
