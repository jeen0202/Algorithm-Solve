import sys
sys.stdin = open("Baekjoon/Graph/Tomato/input.txt","r")
from collections import deque
M,N = map(int,input().split(" "))
queue=deque()
Graph=[]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    Graph.append(list(map(int,input().split(" "))))
for i in range(N):
    for j in range(M):
        if Graph[i][j] == 1:
            queue.append([i,j])
def BFS(queue=queue,Graph=Graph):
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if Graph[nx][ny] == 0:
                    Graph[nx][ny] = Graph[x][y]+1
                    queue.append([nx,ny])
print(Graph)

ans=0
BFS()
for i in Graph:
    for j in i:
        if j ==0:
            print(-1)
            exit(0)
    ans = max(ans,max(i))
print(ans-1)


