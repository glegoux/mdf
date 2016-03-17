n = int(input())
P = {tuple(map(int, input().split())) for _ in range(n)}
d = 0

import math

root = next(iter(P))
S = set([root])
D = dict()
N = dict()
for p in P - S:
    N[p] = root
    D[p] = math.sqrt((p[0] - root[0]) ** 2 + (p[1] - root[1]) ** 2)
local_print(D)

while len(S) != len(P):
    Min, Dist = min(D.items(), key=lambda x: x[1])
    local_print(str(Min) + " " + str(Dist))
    d += Dist
    del D[Min]
    S.add(Min)
    for p in P - S:
        newD = math.sqrt((p[0] - Min[0]) ** 2 + (p[1] - Min[1]) ** 2)
        if D[p] > newD:
            N[p] = Min
            D[p] = newD
print(d)

