import sys
sys.stdin = open("Baekjoon/Graph/EasyShortcut/input.txt","r")
from collections import deque
n,m  = map(int,input().split(" "))
p = []
visited = [[-1 for _ in range(m)]for _ in range(n)]
for i in range(n):
    p.append(list(map(int,input().split(" "))))
    for j in range(m):
        if p[i][j] == 2:
            sx,sy = (i,j)
        if p[i][j] == 0:
            visited[i][j] = 0
visited[sx][sy] = 0
dd = [(-1,0),(1,0),(0,-1),(0,1)]
#bfs
q = deque()
q.append((sx,sy))
while q:
    x,y = q.popleft()
    for i in range(4):
        dx,dy = (sum(e) for e in zip(dd[i],(x,y)))
        if 0<=dx<n and 0<=dy<m and visited[dx][dy] == -1:
            visited[dx][dy] = visited[x][y] +1
            q.append((dx,dy))
for line in visited:
    print(" ".join(map(str,line)))