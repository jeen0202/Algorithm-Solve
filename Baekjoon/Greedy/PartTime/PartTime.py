import sys
sys.stdin = open("Baekjoon/Greedy/PartTime/input.txt","r")
n = int(input())
tips = [int(input()) for _ in range(n)]
tips.sort(reverse=True)
ans = 0
for i in range(n):
    temp = tips[i] -i
    ans+= max(temp,0)
print(ans)