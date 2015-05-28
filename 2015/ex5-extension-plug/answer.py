#!/usr/bin/env python3

##
#  ex5-extension-plug/ :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

N = int(lines[0])
del lines[0]

plugs = dict()
plugs['F-M'] = list()
plugs['M-F'] = list()
plugs['M-M'] = list()
plugs['F-F'] = list()
for line in lines:
    l = line.split(' ')
    _type = l[0]
    _len = int(l[1])
    plugs[_type].append(_len)

for plug in plugs.values():
    plug.sort()
    plug.reverse()

longest = sum(plugs['F-M']) + sum(plugs['M-F'])
mm = len(plugs['M-M'])
ff = len(plugs['F-F'])
if mm < ff:
    longest += sum(plugs['M-M']) + sum(plugs['F-F'][:mm])
else:
    longest += sum(plugs['F-F']) + sum(plugs['M-M'][:ff])

print(longest)
