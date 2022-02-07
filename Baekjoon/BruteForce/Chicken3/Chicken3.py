import sys
sys.stdin = open("Baekjoon/BruteForce/Chicken3/input.txt","r")
from itertools import combinations
n,m = map(int,input().split(" "))
p = [tuple(map(int,input().split(" "))) for _ in range(n)]
comb = list(combinations(range(m),3))
ans = 0
for sel in comb:
    arr = [0 for _ in range(n)]
    for i in range(n):
        arr[i] = max(p[i][sel[0]],p[i][sel[1]],p[i][sel[2]])
    ans = max(ans,sum(arr))
print(ans)