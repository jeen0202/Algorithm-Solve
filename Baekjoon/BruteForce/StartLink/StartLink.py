import sys
sys.stdin = open("Baekjoon/BruteForce/StartLink/input.txt","r")
from itertools import combinations
n = int(input())
p = [list(map(int,input().split(" ")))for _ in range(n)]
ans = sys.maxsize
for i in combinations(range(n),n//2):
    team_a = [*i]
    team_b = list(set(range(n))-set(team_a))
    sa,sb = 0,0
    for j,k in combinations(team_a,2):
        sa+= p[j][k] + p[k][j]
    
    for j,k in combinations(team_b,2):
        sb += p[j][k] + p[k][j]
    cal = abs(sa-sb)

    if cal == 0:
        print(0)
        exit()
    elif cal <= ans:
        ans = cal

print(ans)