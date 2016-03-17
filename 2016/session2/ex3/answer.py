#!/usr/bin/env python3

##
#  ex3 :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

def damerau_levenshtein_distance(a, b):
    n = len(a)
    m = len(b)
    dist = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if min(i, j) == 0:
                dist[i][j] = max(i, j) * 2
            elif i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                dist[i][j] = min(dist[i - 1][j] + 2,
                                 dist[i][j - 1] + 2,
                                 dist[i - 1][j - 1] + 3 * (a[i - 1] != b[j - 1]),
                                 dist[i - 2][j - 2] + 3)
            else:
                dist[i][j] = min(dist[i - 1][j] + 2,
                                 dist[i][j - 1] + 2,
                                 dist[i - 1][j - 1] + 3 * (a[i - 1] != b[j - 1]))
    return dist[n][m]

N = int(input())
words = []
for _ in range(N):
    words.append(input())
M = int(input())
for _ in range(M):
    contestants = []
    s = input()
    for i in range(N):
        contestants.append((damerau_levenshtein_distance(s, words[i]), words[i]))
    _, answer = min(contestants)
    print(answer)
