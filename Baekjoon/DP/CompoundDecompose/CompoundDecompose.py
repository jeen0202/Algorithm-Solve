import sys
sys.stdin = open("Baekjoon/DP/CompoundDecompose/input.txt","r")
input = sys.stdin.readline
n,k = map(int,input().split())
dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
dp[0][0] = 1
for j in range(1,k+1):
    for l in range(n+1):
        dp[j][l] = (dp[j][l-1]+dp[j-1][l])%1000000000
print(dp[k][n])