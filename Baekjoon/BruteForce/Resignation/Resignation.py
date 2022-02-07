import sys
sys.stdin = open("Baekjoon/BruteForce/Resignation/input.txt","r")
from itertools import combinations
n = int(input())
p = [tuple(map(int,input().split(" "))) for _ in range(n)]
comb = []
for i in range(1,n+1):
    comb.extend(list(combinations(range(n),i)))
ans = 0
for sel in comb:
    cnt = 0
    income= 0
    for day in sel:
        if cnt >day:
            continue
        if day+p[day][0] > n:
            continue
        income += p[day][1]
        cnt = day+p[day][0]
    ans = max(ans,income)
print(ans)