import sys
sys.stdin = open("Baekjoon/Graph/Bomberman/input.txt","r")
from collections import deque
R,C,N = map(int,input().split(" "))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
Graph = []
queue = deque()
for i in range(R):
    Graph.append(list(map(str,input())))
    for j in range(C):
        if Graph[i][j] == 'O':
            queue.append([i,j])
#변환
def Check(Graph):
    for i in range(R):
        for j in range(C):
            if Graph[i][j] == 'O':
                #Graph[i][j] = '.'
                queue.append([i,j])

def BFS(time,queue=queue,Graph=Graph):
    now = 0
    Check(Graph)
    while time-1 != now:
        now+=1
        if now%2 == 0:
            while queue:
                x,y = queue.popleft()
                Graph[x][y] ='.'
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if 0<=nx<R and 0<=ny<C:
                        Graph[nx][ny] = '.'
            queue.clear()
            Check(Graph)
        else:
            Graph = [['O' for _ in range(C)] for _ in range(R)]
    return Graph
Graph = BFS(N)
for line in Graph:
    print("".join(line))