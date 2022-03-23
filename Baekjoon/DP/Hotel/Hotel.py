import sys
sys.stdin = open("Baekjoon/DP/Hotel/input.txt","r")
input = sys.stdin.readline
c,n = map(int,input().split())
check = 0
towns = [list(map(int,input().split())) for _ in range(n)]
towns.sort(key = lambda x : x[0])
dp = [sys.maxsize]*(c+100)
dp[0] = 0
for i in range(n):
    for j in range(towns[i][1],c+100):
        dp[j] = min(dp[j-towns[i][1]]+towns[i][0],dp[j])
print(min(dp[c:]))