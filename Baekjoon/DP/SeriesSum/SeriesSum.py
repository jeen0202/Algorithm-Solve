import sys
sys.stdin = open("Baekjoon/DP/SeriesSum/input.txt","r")

def solution():
    N = int(input())
    p = list(map(int,input().split()))
    dp = [0]* N
    dp[0] = p[0]
    for i in range(1,N):
        dp[i] = (max(p[i],dp[i-1]+p[i]))
    print(max(dp))

if __name__ == "__main__" :
    solution()