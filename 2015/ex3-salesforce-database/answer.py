#!/usr/bin/env python3

##
#  ex3-salesforce-database/ :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys
import re

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

N = int(lines[0])
del lines[0]
countries = lines[0].split(';')
del lines[0]

X = 0
Y = 0
Z = 0
db = dict()
for line in lines:
    formated_line = line.split(';')
    i = formated_line[0]  + ";"  + formated_line[1] + ";" + formated_line[2]
    phone = formated_line[3]
    country = formated_line[4]

    if db.get(i) is None:
        db[i] = True
    else:
        X += 1
        continue

    if re.search("^\+[0-9]{1,3}-[0-9]{9,11}$", phone) is None:
        Y += 1

    if country not in countries:
        Z += 1

print(X, Y, Z)
