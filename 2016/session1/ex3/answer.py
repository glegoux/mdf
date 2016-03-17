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

total = int(lines[0])
del lines[0]
N = int(lines[0])
del lines[0]

system = []
for i in range(N):
    nb, amount = map(int, lines[i].split(' '))
    for _ in range(nb):
        system.append(amount)
nb_coins = len(system)

min_coins = []
for _ in range(nb_coins + 1):
  min_coins.append([float('inf')] * (total + 1))
min_coins[0][0] = 0

for i in range(1, nb_coins + 1):
    for j in range(total + 1):
        if j == 0:
            min_coins[i][j] = 0
        else:
            best = min_coins[i - 1][j]
            if j >= system[i - 1]:
                best = min(best, 1 + min_coins[i - 1][j - system[i - 1]])
            min_coins[i][j] = best

if min_coins[nb_coins][total] == float('inf'):
    print('IMPOSSIBLE')
else:
    print(min_coins[nb_coins][total])

