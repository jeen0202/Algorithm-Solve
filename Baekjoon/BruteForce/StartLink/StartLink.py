import sys
sys.stdin = open("Baekjoon/BruteForce/StartLink/input.txt","r")
import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
arr = [i for i in range(n)]
p = [list(map(int,input().split()))for _ in range(n)]
ans = sys.maxsize
for i in range(n):
    for a in combinations(arr,i):
        sa,sb = 0,0
        b = list(set(arr) - set(a))
        for r in combinations(a,2):
            sa += (p[r[0]][r[1]] + p[r[1]][r[0]])
        for r in combinations(b,2):
            sb += (p[r[0]][r[1]] + p[r[1]][r[0]])
        ans = min(ans,abs(sa-sb))
        if ans == 0:
            break
print(ans)