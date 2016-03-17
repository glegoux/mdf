import sys
sys.setrecursionlimit(1000000000)
n=int(input())
g=[[] for _ in range(n)]
for i in range(n-1):
    u,v=map(int,input().split())
    g[u]+=[v]
    g[v]+=[u]
     
prof=[0 for i in range(n)]
def find(a,b):
    v=1
    for c in g[a]:
        if c!=b:
            v+=find(c,a)
    prof[a]=v
    return(v)
    
mini=1000000000
    
def find2(a,b,w):
    global mini
    v=w
    for c in g[a]:
        if c!=b:
            v=max(v,prof[c])
            find2(c,a,w+prof[a]-prof[c])
    mini=min(mini,v)
    
x=find(0,-1)
find2(0,-1,0)
print(mini)


