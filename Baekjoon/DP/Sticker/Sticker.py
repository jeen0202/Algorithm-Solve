import sys
sys.stdin = open("Baekjoon/DP/Sticker/input.txt","r")
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int,input().split())))
    dp = [[0 for _ in range(n)]for _ in range(2)]      
    dp[0][0],dp[1][0] = sticker[0][0],sticker[1][0]
    if n>=2:
        dp[0][1] = max(sticker[0][0],sticker[1][0]+sticker[0][1])
        dp[1][1] = max(sticker[1][0],dp[0][0]+sticker[1][1])
        for i in range(2,n):
            dp[0][i] = max(dp[0][i-1],dp[1][i-1]+sticker[0][i])
            dp[1][i] = max(dp[1][i-1],dp[0][i-1]+sticker[1][i])
    print(max(max(dp[0]),max(dp[1])))