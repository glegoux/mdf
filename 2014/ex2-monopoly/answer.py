#!/usr/bin/env python3

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

c = 0
s = int(lines[0])
b = list(map(int, lines[1].split(' ')))
d = list(map(int, lines[2].split(' ')))
for t in range(len(d)//2):
    dd = d[2*t] + d[2*t+1]
    c = (c + dd) % 40
    s = s - b[c]
    if c == 19:
        c = 9
    if s < 0:
        print(c+1)
        break
