import sys
sys.stdin = open("./Baekjoon/Graph/Virus/input.txt","r")
from collections import defaultdict,deque
N = int(input())
M = int(input())
p = defaultdict(list)
cnt = 0
for _ in range(M):
    node = list(map(int,input().split(" ")))
    p[node[0]].append(node[1])
    p[node[1]].append(node[0])

def bfs(start,graph):
    global cnt
    visited = []
    queue = deque([start])
    visited.append(start)
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if node not in visited:
                queue.append(node)
                visited.append(node)
                cnt+=1
bfs(1,p)
print(cnt)   


