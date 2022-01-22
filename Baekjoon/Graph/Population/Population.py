import sys
sys.stdin = open("Baekjoon/Graph/Population/input.txt","r")
from collections import deque
dd = [(-1,0),(1,0),(0,-1),(0,1)]
n,l,r = map(int,input().split(" "))
Graph = []
for _ in range(n):
    Graph.append(list(map(int,input().split(" "))))
def DFS(root):
    visited = [[0 for _ in range(n)]for _ in range(n)]
    stack = [root]
    nChange = set()
    while stack:
        x,y = stack.pop()
        if visited[x][y] == 0:
            visited[x][y] = 1
            for i in range(4):
                nx,ny = x+dd[i][0], y+dd[i][1]
                if 0<= nx <n and 0<= ny < n:
                    if l<= abs(Graph[x][y]-Graph[nx][ny]) <=r :
                        stack.append(((nx,ny)))
                        nChange.add((nx,ny))
    output = round(sum(Graph[i[0]][i[1]] for i in nChange)/len(nChange))
    for (ix,iy) in nChange:
        Graph[ix][iy] = output
day = 0

DFS((0,0))
print(Graph)