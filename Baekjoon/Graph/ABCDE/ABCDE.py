import sys
sys.stdin = open("Baekjoon/Graph/ABCDE/input.txt","r")
from collections import defaultdict
n,m = map(int,input().split(" "))
Graph = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split(" "))
    Graph[a].append(b)
    Graph[b].append(a)
visited = []
def DFS(next,visited):
    q = list()
    now,cnt = next
    q.append((now,cnt))
    visited.append(now)
    while(q):
        a,cnt = q.pop()
        for b in Graph[a]:
            if b not in visited:
                if cnt+1 == 5:
                    print(1)
                    exit()
                DFS((b,cnt+1),visited)
for i in range(n):
    visited = []
    DFS((i,1),visited)
print(0)
exit()
    
