import sys
sys.stdin = open("Baekjoon/DP/Pinary/input.txt","r")

def solution():
    n = int(input())
    dp = [0] * n
    dp[0] = 1
    if n >= 2:
        dp[1] = 1
    for i in range(2,n):
        dp[i] = dp[i-1]+dp[i-2]
    print(dp[n-1])

if __name__ == "__main__":
    solution()
    