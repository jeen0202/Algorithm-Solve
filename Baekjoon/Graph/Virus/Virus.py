import sys
sys.stdin = open("./Baekjoon/Graph/Virus/input.txt","r")
from collections import defaultdict
N = int(input())
M = int(input())
p = defaultdict(list)
for _ in range(M):
    node = list(map(int,input().split(" ")))
    p[node[0]].append(node[1])
    p[node[1]].append(node[0])
cnt = 0
def dfs(start,graph,visited = []):
    global cnt
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(node,graph,visited)
            cnt +=1

dfs(1,p)
print(cnt)       


