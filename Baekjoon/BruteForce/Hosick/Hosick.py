import sys
sys.stdin = open("Baekjoon/BruteForce/Hosick/input.txt","r")
from itertools import combinations
n,m = map(int,input().split())
roads = [[sys.maxsize]*n for _ in range(n)]
hss = list(combinations(range(n),2))
# 플로이드-와샬
for _ in range(m):
    a,b = map(int,input().split())
    roads[a-1][b-1] = 2
    roads[b-1][a-1] = 2 
for i in range(n):
    roads[i][i] = 0
for k in range(n):
    for j in range(n):
        for i in range(n):
            roads[i][j] = min(roads[i][j],roads[i][k] + roads[k][j])
ans = sys.maxsize
ac = [-1,-1]
for c1,c2 in hss:
    temp = 0
    for b in range(n):
        temp += min(roads[b][c1],roads[b][c2])
    if ans > temp:
        ans = temp
        ac = [c1,c2]

print(ac[0]+1, ac[1]+1, ans)