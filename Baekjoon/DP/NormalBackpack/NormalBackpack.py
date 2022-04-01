import sys
sys.stdin = open("Baekjoon/DP/NormalBackpack/input.txt","r")
input = sys.stdin.readline
n,k = map(int,input().split())
g = [[0,0]]
for _ in range(n):
    g.append(list(map(int,input().split())))
dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        w,v = g[i]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[n][k])