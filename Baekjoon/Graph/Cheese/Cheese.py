import sys
sys.stdin = open("Baekjoon/Graph/Cheese/input.txt","r")
from collections import deque
n,m = map(int,input().split(" "))
p = []
dd = [(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(n):
    p.append(list(map(int,input().split(" "))))

def bfs():
    visited = []
    visited.append((0,0))
    q = deque()
    q.append((0,0))
    cnt = 0
    while q:
        cnt+1
        x,y = q.popleft()
        for i in range(4):
            dx,dy = (sum(e) for e in zip(dd[i],(x,y)))
            if 0<=dx<n and 0<=dy<m and (dx,dy) not in visited:
                visited.append((dx,dy))
                if p[dx][dy] != 1:
                    q.append((dx,dy))
                else :
                    p[dx][dy] = 0
                    cnt+=1
    return cnt
hour = 0
while True:
    temp = bfs()
    if temp == 0:
        break
    hour += 1
    c = temp
print(hour)
print(c)