
import sys
sys.stdin = open("Baekjoon/Graph/Tomato2/input.txt","r")
from collections import deque
m,n,k = map(int,input().split(" "))
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
Graph = [[[0 for _ in range(m)]for _ in range(n)] for _ in range(k)]
visited= deque()
for i in range(k):
    for j in range(n):
        Graph[i][j] = list(map(int,input().split(" ")))
        for l in range(m):
            if Graph[i][j][l] == 1:
                visited.append((i,j,l))
def Check(Graph):
    ans = 0
    for box in Graph:
        for line in box:
            if line.count(0):
                return -1
            ans = max(ans,max(line))
    return ans-1

def BFS():
    while visited:
        z,x,y = visited.popleft()
        for i in range(6):
            nx,ny,nz = x + dx[i], y + dy[i], z+dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<k:
                if Graph[nz][nx][ny] == 0:
                    Graph[nz][nx][ny] = Graph[z][x][y]+1
                    visited.append((nz,nx,ny))
BFS()
print(Check(Graph))