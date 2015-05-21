#!/usr/bin/env python3

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

p = int(lines[0])
rmin = list()
for i in range(1,p+1):
    r = list(map(int, lines[i].split(' ')))
    xmin = min(r[0], r[2])
    xmax = max(r[0], r[2])
    ymin = min(r[1], r[3])
    ymax = max(r[1], r[3])
    if i == 1:
        rmin = [xmin, xmax, ymin, ymax]
        continue
    if xmin < rmin[0]:
        rmin[0] = xmin
    if xmax > rmin[1]:
        rmin[1] = xmax
    if ymin < rmin[2]:
        rmin[2] = ymin
    if ymax > rmin[3]:
        rmin[3] = ymax
print(rmin[0], rmin[2], rmin[0], rmin[3], rmin[1], rmin[2], rmin[1], rmin[3])
