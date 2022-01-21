import sys
sys.stdin = open("Baekjoon/Graph/Laboratory/input.txt","r")
import copy
from collections import deque
from itertools import combinations
N,M = map(int,input().split(" "))
Graph = []
dd = [(-1,0),(1,0),(0,-1),(0,1)]
Virus,zeros = deque(),deque()
for i in range(N):
    Graph.append(list(map(int,input().split(" "))))
    for j in range(M):
        if Graph[i][j] == 2:
            Virus.append((i,j))
        elif Graph[i][j] == 0:
            zeros.append((i,j))
newWalls = list(combinations(zeros,3))

def BFS(graph):
    virus = copy.deepcopy(Virus)
    while virus:
        x,y = virus.popleft()
        for i in range(4):
            nx,ny = (sum(elem) for elem in zip(dd[i],(x,y)))
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                    graph[nx][ny] =2
                    virus.append((nx,ny))
    return graph

def CheckZeros(graph):
    ans = 0
    for line in graph:
        ans+= line.count(0)
    return ans

maxSafe = 0
for newWall in newWalls:
    graph = copy.deepcopy(Graph)
    for nw in newWall:
        graph[nw[0]][nw[1]] = 1
    maxSafe = max(maxSafe,CheckZeros(BFS(graph)))
print(maxSafe)