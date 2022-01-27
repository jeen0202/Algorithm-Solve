import sys
sys.stdin = open("Baekjoon/Graph/ABCDE/input.txt","r")
n,m = map(int,input().split(" "))
Graph = [[]for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split(" "))
    Graph[a].append(b)
    Graph[b].append(a)
    
visited = [False for _ in range(n)]

def DFS(now,cnt):
    visited[now] = True
    if cnt >= 4:
        print(1)
        exit()
    for next in Graph[now]:
        if not visited[next]:
            DFS(next,cnt+1)
            visited[next] = False

for i in range(n):
    DFS(i,0)
    visited[i] = False
print(0)
exit()
