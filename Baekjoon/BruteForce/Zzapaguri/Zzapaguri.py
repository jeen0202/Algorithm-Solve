import sys
sys.stdin = open("Baekjoon/BruteForce/Zzapaguri/input.txt","r")
from itertools import combinations
n = int(input())
p = [list(map(int,input().split(" "))) for _ in range(n)]
temp = []
ret = 1000000000
for i in range(1,n+1):
    temp.extend(combinations(range(n),i))
for food in temp:
    s,b = 0,0
    for item in food:
        s = max(s+p[item][0],s*p[item][0])
        b += p[item][1]
    ret = min(ret,abs(s-b))
print(ret)