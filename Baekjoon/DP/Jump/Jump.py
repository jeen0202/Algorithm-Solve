import sys
sys.stdin = open("Baekjoon/DP/Jump/input.txt","r")
input = sys.stdin.readline
n = int(input())
board = []
dp = [[0]*(n) for _ in range(n)]
for _ in range(n):
    board.append(list(map(int,input().split())))
answer = 0
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1 :
            print(dp[i][j])
            exit()
        now = board[i][j]
        if j + now <n:
            dp[i][j + now] += dp[i][j]
        if i + now < n:
            dp[i+now][j] += dp[i][j]