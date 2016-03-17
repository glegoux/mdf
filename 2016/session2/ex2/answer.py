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

from collections import Counter

s = input()
n = len(s)
letters = []
c = Counter()
i = 0
while i < n:
    if s[i] == '-':
        i += 1
        letters.pop()
    else:
        letters.append(s[i])
        c[s[i]] += 1 / len(letters)
    i += 1
print(min((-v, k) for k, v in c.items())[1])
