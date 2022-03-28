import sys
sys.stdin = open("Baekjoon/DP/SteppingStone/input.txt","r")
input = sys.stdin.readline
n = int(input())
jumps = []
dp = [sys.maxsize]*21
dp[0]=0
for i in range(n-1):
    jump1,jump2 = map(int,input().split())
    jumps.append([jump1,jump2])
    if i+1 <n : dp[i+1] = min(dp[i+1],dp[i]+jump1)
    if i+2 <n : dp[i+2] = min(dp[i+2], dp[i]+jump2)
k = int(input())
# dp = [0]*(21)
# dp[1] = jumps[0][0]
# if n >1:
#     dp[2] = min(jumps[0][0]+jumps[1][0],jumps[0][1]) 
#     for i in range(3,n):
#         dp[i] = min(dp[i-1]+jumps[i-1][0],dp[i-2]+jumps[i-2][1])

        
        
_min = dp[n-1]
for i in range(3 ,n):
    e = dp[i-3]+k
    dp1, dp2 = sys.maxsize, sys.maxsize
    for j in range(i, n-1):
        if i+1<=n : dp1 = min(dp1, e+jumps[j][0])
        if i+2<=n : dp2 = min(dp2, e+jumps[j][1])
        e, dp1, dp2 = dp1, dp2, sys.maxsize
    _min = min(_min, e)
print(_min)