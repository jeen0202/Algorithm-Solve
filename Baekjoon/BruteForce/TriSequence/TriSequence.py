
import sys
sys.stdin = open("Baekjoon/BruteForce/TriSequence/input.txt","r")

n = int(input())
p = list(map(int,input().split(" ")))
p.sort()
ans = 0
if len(p) <3:
    ans=max(ans,len(p))
for i in range(n-2):
    for j in range(i+2,n):
        if p[i] + p[i+1] > p[j] :
            ans = max(ans,j-i+1)
if ans == 0 and len(p)>=3:
    ans = 2        
print(ans)
