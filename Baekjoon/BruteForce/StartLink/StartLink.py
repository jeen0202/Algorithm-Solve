import sys
sys.stdin = open("Baekjoon/BruteForce/StartLink/input.txt","r")
from itertools import combinations
n = int(input())
p = [list(map(int,input().split(" ")))for _ in range(n)]
team = []
for i in range(1,n):
    team.extend(combinations(range(n),i))
ans = sys.maxsize
for a in team:
    sa,sb = 0,0
    for j in range(n):
        sb += sum(p[j])    
    if len(a) ==1:
        sa= 0
    else :
        for i,j in combinations(a,2):
            sa+= p[i][j] + p[j][i]
    sb-=sa
    cal = abs(sa-sb)
    ans = min(ans,cal)
print(ans)