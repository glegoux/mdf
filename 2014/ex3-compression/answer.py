#!/usr/bin/env python3

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

s = lines[0]

if len(s) < 3:
    print(s)
    exit(0)

cs = ''
pc = s[0]
pn = 1
for c in s[1:] + '0':
    if pc == c:
        pn += 1
    else:
        if pn == 1:
            cs = cs + pc
        elif pn == 2:
            cs = cs + pc + pc
        else:
            cs = cs + str(pn) + pc
        pn = 1
    pc = c
print(cs)
