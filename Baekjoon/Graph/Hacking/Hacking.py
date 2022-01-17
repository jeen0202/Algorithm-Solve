from email.policy import default
import sys
sys.stdin = open("baekjoon/Graph/Hacking/input.txt","r")
from collections import defaultdict,deque
N,M = map(int,input().split(" "))
mnode = 0
Graph = defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split(" "))
    Graph[b].append(a)
print(Graph)

def BFS(start,Graph=Graph):
    visited = [False]*(N+1)
    cnt = 1
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for node in Graph[v]:
            if visited[node] == False:
                cnt +=1
                visited[node] = True
                queue.append(node)
    return cnt

ans = []
for i in range(1,N+1):
    res = BFS(i)
    if mnode < res:
        ans = [i]
        mnode = res
        continue
    if mnode == res:
        ans.append(i)
ans.sort()
print(" ".join(map(str,ans)))
