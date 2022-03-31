import sys
sys.stdin = open("Baekjoon/DP/District/input.txt","r")
input = sys.stdin.readline
n,m = map(int,input().split())
grounds = []
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for _ in range(n):
    grounds.append(list(map(int,input().split())))
for i in range(1,n+1):
    for j in range(1,m+1):
        if j == 1:
            dp[i][j] = grounds[i-1][j-1]
        dp[i][j] = dp[i][j-1]+grounds[i-1][j-1]
k = int(input())
for _ in range(k):
    ans = 0
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2+1):
        ans += dp[i][y2] - dp[i][y1-1]
    print(ans)