#!/usr/bin/env python3

##
#  ex3-compression/ :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

s = lines[0]

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
