#!/usr/bin/env python3

##
#  ex1-poker/ :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

S = int(lines[0])
del lines[0]
N = int(lines[0])
del lines[0]

account=S
for line in lines:
    X = int(line.split(' ')[0])
    Y = int(line.split(' ')[1])
    account = account - X + Y 

print(account)
