import sys
sys.stdin = open("Baekjoon/DP/Coin_1/input.txt","r")
input = sys.stdin.readline
n,k = map(int,input().split())
coins = []
dp = [0]*(k+1)
dp[0]=1
for _ in range(n):
    coin = int(input())
    coins.append(coin)
for coin in coins:
    for i in range(1,k+1):
        if i-coin >=0 and dp[i-coin]>0:
            dp[i] += dp[i-coin]
print(dp[k])