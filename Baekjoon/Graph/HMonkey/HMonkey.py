import sys
from tkinter import W
sys.stdin = open("Baekjoon/Graph/HMonkey/input.txt","r")
k = int(input())
w,h = map(int,input().split(" "))
dd = [(-1,0),(1,0),(0,-1),(0,1)]
kk = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
graph = []
visited = [[False for _ in range(w)]for _ in range(h)]
for _ in range(h):
    graph.append(list(map(int,input().split(" "))))
cnt =0
def DFS(start,visited,k,cnt):
    x,y = start
    if (x,y) == (h-1,w-1):
        return cnt 
    visited[x][y] = True
    for i in range(4):
        nx,ny = x+dd[i][0], y+dd[i][1]
        if 0<=nx < h and 0<= ny <w:
            if visited[nx][ny] == False and graph[nx][ny] == 0:
                DFS((nx,ny),visited,k,cnt+1)
                visited[x][y] = False
    if k > 0:
        for j in range(8):
            kx,ky = x+kk[j][0],y+kk[j][1]
            if 0<=kx<h and 0<= ky <w:
                if visited[kx][ky] == False and graph[kx][ky] ==0:
                    DFS((kx,ky),visited,k-1,cnt+1)
                    visited[x][y] = False
    return 0
sys.setrecursionlimit(10000**2)
print(DFS((0,0),visited,k,cnt))