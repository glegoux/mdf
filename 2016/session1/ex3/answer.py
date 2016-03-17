#!/usr/bin/env python3

##
#  ex3 :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
      lines.append(line.rstrip('\n'))

M = lines[0]
del lines[0]

vs = []
q = {}
for l in lines:
  v, q = list(map(int, l.split(' ')))
  vs.append(v)
  q[v] = q

vs.sort(reversed=True)


k = 0
o = 0
while M > q[k]:
    for i, v in enumerate(vs):
        if v > M and q[v] != 0:
          M -= v
          o += 1
          k = i
print(o)

