#!/usr/bin/env python3

import sys

input = list()
for line in sys.stdin:
    input.append(line.rstrip('\n'))

s=sum(list(map(int, input)))

if s % 6 == 1:
    print("orange")
elif s % 6 == 2:
    print("jaune")
elif s % 6 == 3:
    print("vert")
elif s % 6 == 4:
    print("rose")
elif s % 6 == 5:
    print("bleu")
else:
    print("violet")
