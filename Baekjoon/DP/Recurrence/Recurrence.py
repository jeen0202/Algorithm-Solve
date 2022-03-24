import sys
sys.stdin = open("Baekjoon/DP/Recurrence/input.txt","r")
input = sys.stdin.readline
n = int(input())
dp = [0]*(36)
dp[0] = 1
for i in range(1,n+1):
    for j in range(i):
        dp[i] += dp[j]*(dp[i-1-j])
print(dp[n])