import sys
sys.stdin = open("Baekjoon/DP/2XN_Tile2/input.txt","r")
n = int(input())
dp = [0]*1001
dp[1] = 1
dp[2] = 3
for i in range(3,n+1):
    dp[i] = dp[i-1]+(dp[i-2]*2)
print(dp[n] %10007)