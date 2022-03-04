import sys
sys.stdin = open("Baekjoon/Greedy/Rope/input.txt","r")
n = int(input())
weights = [int(input()) for _ in range(n)]
weights.sort(reverse=True)
ans = 0
for i in range(n):
    if weights[i]*(i+1) >= ans:
        ans = weights[i]*(i+1)
print(ans)
