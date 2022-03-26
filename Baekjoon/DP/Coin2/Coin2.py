from asyncio import coroutines
import sys
sys.stdin = open("Baekjoon/DP/Coin2/input.txt","r")
input = sys.stdin.readline
n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [sys.maxsize] * 100001
dp[0] = -1
for item in coins:
    dp[item] = 1
for i in range(1,k+1):
    for coin in coins:
        if i-coin >0:
            dp[i] = min(dp[i],dp[i-coin]+1)
if dp[k] == sys.maxsize:
    print(-1)
    exit()
print(dp[k])