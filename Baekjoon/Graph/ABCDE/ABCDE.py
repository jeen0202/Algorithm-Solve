import sys
sys.stdin = open("Baekjoon/Graph/ABCDE/input.txt","r")
from collections import defaultdict,deque
n,m = map(int,input().split(" "))
Graph = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split(" "))
    Graph[a].append(b)
    Graph[b].append(a)
print(Graph)
for i in range(n):
    visited = []
    q = list()
    cnt = 0
    q.append((i,1))
    visited.append(i)
    while(q):
        a,cnt = q.pop()
        for b in Graph[a]:
            if b not in visited:
                if cnt+1 >= 5:
                    print(1)
                    exit()
                visited.append(b)
                q.append((b,cnt+1))
print(0)
exit()
    
