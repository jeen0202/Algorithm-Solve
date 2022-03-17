import sys
sys.stdin = open("Baekjoon/DP/StairsGame/input.txt","r")
input = sys.stdin.readline
n = int(input())
stairs = [int(input()) for _ in range(n)]
if n <3:
    print(sum(stairs))
    exit()
dp = [0]*n
dp[0] = stairs[0]
dp[1] = stairs[0]+stairs[1]
dp[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])
for i in range(3,n):
    dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])
print(dp.pop())