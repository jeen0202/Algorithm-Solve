import sys
sys.stdin = open("Baekjoon/DP/LongestSequence/input.txt","r")
n,k = map(int,input().split())
s = list(map(int,input().split()))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n):
    s[i] %=2
    for j in range(k+1):
        if s[i] == 0:
            dp[i+1][j] = dp[i][j]+1
        if j!= 0 and s[i]:
            dp[i+1][j] = dp[i][j-1]
result = []
for i in dp:
    result.append(i[k])
print(max(result))