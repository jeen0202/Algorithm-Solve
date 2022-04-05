import sys
sys.stdin = open("Baekjoon/DP/LineUp/input.txt","r")
input = sys.stdin.readline
n = int(input())
graph = [int(input()) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n+1)]
check = 0
for i in range(n):
    dp[i][i] = 1
    for j in range(i+1,n):
        for k in range(j):
            if graph[k] < graph[j]:
                dp[i][j] = max(dp[i][j],dp[i][k]+1)
    check = max(check,max(dp[i]))
ans = n-check
print(ans)
