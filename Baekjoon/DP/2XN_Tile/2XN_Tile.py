import sys
sys.stdin = open("Baekjoon/DP/2XN_Tile/input.txt","r")
n = int(input())
dp = [0]*1001
dp[0] = 0
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n]%10007)

