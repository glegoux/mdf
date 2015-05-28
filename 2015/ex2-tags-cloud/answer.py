#!/usr/bin/env python3

##
#  ex2-tags-cloud/ :
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

d = dict()
for tag in lines:
    if d.get(tag) is None:
        d[tag] = 1
    else:
        d[tag] += 1

nbs = list()
for tag, nb in d.items():
    nbs.append(nb)

nbs.sort()
nbs.reverse()
nbs = nbs[:5]

for nb in nbs:
    for tag, _nb in d.items():
        if nb == _nb: 
            print(tag, nb)
