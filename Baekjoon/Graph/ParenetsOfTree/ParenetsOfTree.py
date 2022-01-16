import sys
sys.stdin = open("./Baekjoon/Graph/ParenetsOfTree/input.txt","r")
from collections import defaultdict,deque
N = int(input())
parents=[0]*(N+1)
Graph = defaultdict(list)
for _ in range (N-1):
    a,b = map(int,input().split(" "))
    Graph[a].append(b)
    Graph[b].append(a)

def DFS(start,visited=[],Graph=Graph):
    visited.append(start)
    for v in Graph[start]:
        if v not in visited:
            visited.append(v)
            parents[v] = start
            DFS(v,visited)
    
DFS(1)
for item in parents[2:]:
    print(item)