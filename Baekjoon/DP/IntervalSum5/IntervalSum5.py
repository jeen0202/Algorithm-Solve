import sys
sys.stdin = open("Baekjoon/DP/IntervalSum5/input.txt","r")
input = sys.stdin.readline
n,m = map(int,input().split())
matrix = [list(map(int,input().split()))for _ in range(n)]

for _ in range(m):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    x1,y1,x2,y2 = map(int,input().split())
    dp[x1-1][y1-1] = matrix[x1-1][y1-1]
    for i in range(x1-1,x2):
        for j in range(y1,y2):
                dp[i][j] = dp[i][j-1]+matrix[i][j]
        if i+1 <n:
            dp[i+1][y1-1] = matrix[i+1][y1-1]+dp[i][n-1]
    print(dp[x2-1][y2-1])   