import sys
sys.stdin = open("Baekjoon/Greedy/A2B/input.txt","r")
from collections import deque
a,b  = map(int,input().split())
ans = -1
q = deque([(a,1)])
while q:
    c,cnt = q.popleft()
    if c == b:
        ans = cnt
        break    
    if c*2 <= b:
        q.append((c*2,cnt+1))
    hap = str(c)+'1'
    if int(hap)<=b:
        q.append((int(hap),cnt+1))
print(ans)
