import sys
sys.stdin = open("Baekjoon/Greedy/Muscle/input.txt","r")
input = sys.stdin.readline
n = int(input())
t = list(map(int,input().split()))
t.sort()
ans = 0
if n%2 == 0:
    for i in range(n//2):
        ans = max(ans,t[i]+t[-i-1])
else:
    for i in range(n//2):
        ans = max(ans,t[i]+t[-i-2])
    ans = max(ans,t[-1])
print(ans)