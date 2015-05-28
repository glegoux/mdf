#!/usr/bin/env python3

##
#  ex4-trending-topics/ :
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
for n, tag in enumerate(lines):
    if d.get(tag) is None:
        d[tag] = 1
    else:
        d[tag] += 1 
        if d[tag] >= 40:
            print(tag)
            break  
  
    if n >= 60:
        out_tag = lines[n-60]
        if d[out_tag] > 0:
            d[out_tag] -= 1
        else:
            del d[out_tag]
else:
    print("Pas de trending topic")
