import sys
sys.stdin = open("Baekjoon/Graph/Fountain/input.txt","r")
from collections import deque
n,k = map(int,input().split(" "))
f = list(map(int,input().split(" ")))
q = deque()
visited = dict()
for i in f:
    visited[i] = 0
    q.append(i)

while q:
    if k <= 0:
        break
    x = q.popleft()
    for dx in [x-1,x+1]:
        if dx not in visited and k >0:
            visited[dx] = visited[x]+1
            k -=1
            q.append(dx)

ans = 0
for value in visited.values():
    ans += value
print(ans)