import sys
sys.stdin = open("Baekjoon/DP/SteppingStoneSmall/input.txt","r")
input = sys.stdin.readline
n,k = map(int,input().split())
stones = list(map(int,input().split()))
dp = [-1]*(n+1)
dp[1] = 1

for i in range(1,n):
    if dp[i] == 1:
        for j in range(i+1,n+1):
            if dp[j] == -1 and (j-i)*(1+abs(dp[i-1]-dp[j-1])) <=k:
                    dp[j]= 1
            if dp[n] == 1:
                break
    if dp[n] == 1:
        break
if dp[n] == 1:
    print("YES")
else:
    print("NO")