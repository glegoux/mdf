#!/usr/bin/env python3

##
#  ex5-center-matrix/ :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

p = int(lines[0])
kmin = p//4
kmax = p-p//4
m = list()
for i in range(2, p+1):
    if i-2 < kmin-1 or i-2 >= kmax-1:
        continue
    cl = map(int, lines[i].split(' ')[kmin:kmax])
    m.extend(list(cl))

m.sort()
n = len(m)
d = {}
for e in m:
    if d.get(e):
        d[e] += 1
    else:
        d[e] = 1
vmax = max(d.values())
modes = list()
for k,v in d.items():
    if v == vmax:
        modes.append(k)

print(m[0], m[-1], (m[n//2-1]+m[n//2])/2, min(modes))
