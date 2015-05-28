#!/usr/bin/env python3

##
#  ex7-life-game/ :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

N = lines[0]
del lines[0]

xmax = 0
ymax = 0
for line in lines:
    l = line.split(' ')
    x2 = int(l[2])
    y2 = int(l[3])
    xmax = max(xmax, x2)
    ymax = max(ymax, y2)

M = list()
for y in range(ymax):
    M.append([0]*xmax)

for line in lines:
    l = line.split(' ')
    x1 = int(l[0])
    y1 = int(l[1])
    x2 = int(l[2])
    y2 = int(l[3])
    for y in range(y1-1,y2):
        M[y][x1-1:x2] = [1]*(x2-x1+1)

def copy(m):
    res = list()
    for y in range(len(m)):
        res.append(list(m[y]))
    return res

def death(m):
    for y in range(len(m)):
        for e in m[y]:
            if e == 1:
                return False
    return True

res = 0
MM = copy(M)
while not(death(M)):
    for y in range(ymax):
        for x in range(xmax):
            if x == 0:
                MM[y][x] = 0
                continue
            if y == 0:
                MM[y][x] = 0
                continue
            if M[y][x-1] == 0 and M[y-1][x] == 0:
                MM[y][x] = 0
            elif M[y][x-1] == 1 and M[y-1][x] == 1:
                MM[y][x] = 1
    M = MM
    MM = copy(M)
    res += 1

print(res)
