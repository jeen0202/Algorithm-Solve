import sys
sys.stdin = open("baekjoon/Graph/Maze/input.txt","r")
from collections import deque
N,M = map(int,input().split(" "))
Graph = []
for _ in range(N):
    Graph.append(list(map(int,input())))

def BFS(Graph=Graph):
    queue = deque()
    queue.append([0,0])
    dxy = [[0,-1],[0,1],[-1,0],[1,0]]
    while queue:
        x,y = queue.popleft()
        for dx,dy in dxy:
            xPos = x+dx
            yPos = y+dy
            if xPos >=0 and xPos <N and yPos >=0 and yPos <M and Graph[xPos][yPos] == 1:
                Graph[xPos][yPos]= Graph[x][y]+1
                queue.append([xPos,yPos])
    print(Graph)
    return(Graph[N-1][M-1])

print(BFS())