import sys
sys.stdin = open("Baekjoon/DP/Resignation2/input.txt","r")
input = sys.stdin.readline
n = int(input())
meets = []
for _ in range(n):
    meets.append(list(map(int,input().split())))
dp = [0 for _ in range(n+1)]

check = 0
for i in range(n):
    check = max(check,dp[i])
    if i+meets[i][0] >n:
        continue
    dp[i+meets[i][0]] = max(check + meets[i][1],dp[i+meets[i][0]])
print(max(dp))