import sys
sys.stdin = open("Baekjoon/DP/SteppingStone/input.txt","r")
input = sys.stdin.readline
n = int(input())
jumps = []
for _ in range(n-1):
    jumps.append(list(map(int,input().split())))
k = int(input())
dp = [0]*(n)
dp[1] = jumps[0][0]
dp[2] = min(jumps[0][0]+jumps[1][0],jumps[0][1]) 
for i in range(3,n):
    dp[i] = min(dp[i-1]+jumps[i-1][0],dp[i-2]+jumps[i-2][1])
_min = dp[n-1]
for i in range(3 ,n):
    split1,split2 = dp[i-3],dp[n-1]-dp[i],
    _min = min(_min,split1+k+split2)
print(_min)