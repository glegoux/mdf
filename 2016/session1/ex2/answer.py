#!/usr/bin/env python3

##
#  ex2 :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
      lines.append(line.rstrip('\n'))

N = int(lines[0])
del lines[0]
P = int(lines[0])
del lines[0]

ss = []

for y in range(N):
    s = [y, 0]
    ss.append(s)

for l in lines:
    head = ss[-1]
    s = [head[0], head[1]]
    if l == 'D':
        s[0] += 1
    if l == 'G':
        s[0] -= 1
    if l == 'H':
        s[1] -= 1
    if l == 'B':
        s[1] += 1
    ss.append(s)

ind_queue = len(ss) - N
loc_queue = ss[ind_queue]

print(loc_queue[0], loc_queue[1])
