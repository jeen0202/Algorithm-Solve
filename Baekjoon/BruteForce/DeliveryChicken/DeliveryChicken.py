import sys
sys.stdin = open("Baekjoon/BruteForce/DeliveryChicken/input.txt","r")
from itertools import combinations
n,m = map(int,input().split())
p = [list(map(int,input().split()))for _ in range(n)]
chicken = []
for i in range(n):
    for j in range(n):
        if p[i][j] == 2:
            chicken.append((i,j))
cks = list(combinations(chicken,m))
ans = sys.maxsize
for ck in cks:
    sum = 0
    for i in range(n):
        for j in range(n):
            if p[i][j] == 1:
                ck_dist = 2*n
                for x,y in ck:
                    ck_dist = min(ck_dist,abs(i-x)+abs(j-y))
                sum += ck_dist
    ans = min(ans,sum)
print(ans)