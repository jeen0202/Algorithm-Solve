import sys
sys.stdin = open("Baekjoon/Greedy/Rope/input.txt","r")
input = sys.stdin.readline
n = int(input())
weights = [int(input()) for _ in range(n)]
weights.sort(reverse=True)
print(max(weights[i]*(i+1) for i in range(n)))
