# /usr/bin/env python3

##
#  ex1-trivial-pursuit/ :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

s=sum(list(map(int, lines)))

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
