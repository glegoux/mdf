#!/usr/bin/env python3

##
#  ex5-extension-plug/ :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

N = lines[0]
del lines[0]

d = dict()
for line in lines:
    t = lines.split(' ')[0]
    l = lines.split(' ')[1] 
    if d.get(t) is None:
        d[t] = [l]
    else:
        d[t].append(l)

res = 0
while N != 0:

    if len(d['M-M']) == 0:
        
    if len(d['F-F']) == 0:
    d['M-F']
    d['F-M']
