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
def dfs(start,graph):
    nvisited, visited = list(),list()

    nvisited.append(start)

    while nvisited:
        node = nvisited.pop()
        if node not in visited:
            visited.append(node)
            nvisited.extend(graph[node])
    return visited
def solution():
    visited = [1]
    if len(p[1])==0:
        print(1)
    else:
        print(len(dfs(1,p))-1)        
        

if __name__ == "__main__":
    solution()

