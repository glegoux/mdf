#!/usr/bin/env python3

##
#  ex6-most-common-word/ :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

def clean_string(s):
    return s.replace(';', ' ').replace(',', ' ').replace('.', ' ').replace("'", ' ').lower()

d = dict()
d_all = dict()
n = len(lines)
for line in lines:
    words = clean_string(line).split()
    for word in words:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1
    for word in set(words):
        if word in d_all.keys():
            d_all[word] += 1
        else:
            d_all[word] = 1

for k,v in d_all.items():
    if v == n:
        del d[k]
    if len(k) == 1:
        del d[k]

values = list(set(d.values()))
values.sort()
values.reverse()
values = values[:3]
dd = dict()
for k,v in d.items():
    if v in values:
        if dd.get(v):
            dd[v].append(k)
        else:
            dd[v] = [k]

for v in values:
    dd[v].sort()

i = 0
for v in values:
    for word in dd[v]:
        print(v, word)
        i += 1
        if i == 3:
            break
    else:
        continue
    break

