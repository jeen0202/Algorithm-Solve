import sys
sys.stdin = open("Baekjoon/Graph/Population/input.txt","r")
from collections import deque
dd = [(-1,0),(1,0),(0,-1),(0,1)]
n,l,r = map(int,input().split(" "))
Graph = []
for _ in range(n):
    Graph.append(list(map(int,input().split(" "))))

def DFS(graph,root):
    nv = [[0 for _ in range(n)]for _ in range(n)]
    nv[root[0]][root[1]] = 1
    #while nv:
    x,y = root
    stack = deque()
    stack.append((x,y))
    while stack:
        s= graph[x][y]
        cnt = 1
        sx,sy = stack.pop()
    for i in range(4):
        nx,ny = (sum(elem) for elem in zip(dd[i],(sx,sy)))
        if 0<=nx<n and 0<=ny<n:
            if l<=abs(graph[nx][ny]-graph[sx][sy]) <=r:
                stack.append((nx,ny))
                s+= graph[nx][ny]
                cnt+=1
                nv[nx][ny] = cnt
    for xx,yy in stack:
        graph[xx][yy] = round(s/cnt)
    print(nv)
DFS(Graph,(0,0))
print(Graph)
