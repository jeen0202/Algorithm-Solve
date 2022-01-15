import sys
sys.stdin = open("./Baekjoon/Graph/DFS_BFS/input.txt","r")
sys.setrecursionlimit(10**8)
from collections import defaultdict,deque
N,M,V = map(int,input().split(" "))
Graph = defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split(" "))
    Graph[a].append(b)
    Graph[b].append(a)
for i in range(N):
    Graph[i+1].sort()
def DFS(start,Graph=Graph,visited=[]):
    visited.append(start)
    for node in Graph[start]:
        if node not in visited:
            DFS(node,Graph,visited)
    return(visited)

def BFS(start,Graph=Graph):
    queue = deque([start])
    answer =  [start]
    visited = [False]*(N+1)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for node in Graph[v]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                answer.append(node)
    return(answer)
ans1 = " ".join(map(str,DFS(V)))
ans2 = " ".join(map(str,BFS(V)))
print(ans1)
print(ans2)