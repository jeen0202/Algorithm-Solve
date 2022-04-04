import sys
sys.stdin = open("Baekjoon/DP/FirstGrader/input.txt","r")
input = sys.stdin.readline
n = int(input())
graph = list(map(int,input().split()))
dp = [[0]*21 for _ in range(n)]
dp[0][graph[0]] = 1
for i in range(1,n):
    for j in range(21):
        if dp[i-1][j] !=0:
           check1 = j+graph[i]
           check2 = j-graph[i]
           if 0 <= check1 <= 20:
            dp[i][check1] += dp[i-1][j]
           if 0 <= check2 <= 20:
            dp[i][check2] += dp[i-1][j]
print(dp[n-2][graph[-1]])