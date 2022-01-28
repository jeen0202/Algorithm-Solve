import sys
sys.stdin = open("Baekjoon/Graph/HMonkey/input.txt","r")
from collections import deque
k = int(input())
w,h = map(int,input().split(" "))
dd = [(-1,0),(1,0),(0,-1),(0,1)]
kk = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
graph = []
visited = [[-1 for _ in range(w)]for _ in range(h)]
for _ in range(h):
    graph.append(list(map(int,input().split(" "))))
cnt = []
q = deque()
q.append((0,0,0))
visited[0][0] = 0
while q:
    x,y,z = q.popleft()
    if (x,y) == (h-1,w-1) and z<=k:        
        cnt.append(visited[x][y])
    for i in range(4):
        dx,dy = (sum(e) for e in zip(dd[i],(x,y)))
        if 0<=dx < h and 0<= dy <w:
            if visited[dx][dy] == -1 and graph[dx][dy] == 0:
                visited[dx][dy] = visited[x][y] +1
                q.append((dx,dy,z))
    if z <k:
        for j in range(8):
            kx,ky = x+kk[j][0],y+kk[j][1]
            if 0<=kx<h and 0<= ky <w:
                if visited[kx][ky] == -1 and graph[kx][ky] == 0:
                    visited[kx][ky] = visited[x][y]+1
                    q.append((kx,ky,z+1)) 

if len(cnt):
    print(min(cnt))
    exit()
print(-1)

for line in visited:
    print(line)
# def DFS(start,v,k,c):
#     x,y = start
#     if x == h-1 and y == w-1:
#          cnt.append(c)
#     v[x][y] = True
#     for i in range(4):
#         nx,ny = x+dd[i][0], y+dd[i][1]
#         if 0<=nx < h and 0<= ny <w:
#             if v[nx][ny] == False and graph[nx][ny] == 0:
#                 DFS((nx,ny),v,k,c+1)
#                 v[x][y] = False
#     if k > 0:
#         for j in range(8):
#             kx,ky = x+kk[j][0],y+kk[j][1]
#             if 0<=kx<h and 0<= ky <w:
#                 if v[kx][ky] == False and graph[kx][ky] ==0:
#                     DFS((kx,ky),v,k-1,c+1)
#                     v[x][y] = False
                    
# sys.setrecursionlimit(10000**2)
# DFS((0,0),visited,k,0)