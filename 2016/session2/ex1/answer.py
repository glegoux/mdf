#!/usr/bin/env python3

##
#  ex1 :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
      lines.append(line.rstrip('\n'))

X = lines[0]
del lines[0]
N = lines[0]
del lines[0]

for l in lines:
    Y = int(lines[0])
    del lines[0]
    X -= Y

print(X)
