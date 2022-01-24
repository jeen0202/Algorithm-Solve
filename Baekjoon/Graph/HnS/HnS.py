import sys
sys.stdin = open("Baekjoon/Graph/HnS/input.txt","r")
from collections import deque
n,k = map(int,input().split(" "))
visited = [-1 for _ in range(100001)]

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        x = q.popleft()
        if x == k :
            print(visited[x])
            break
        if (0<= x-1 <= 100000) and visited[x-1]==-1:
            visited[x-1] = visited[x]+1
            q.append(x-1)            
        if (0<= x*2 <= 100000) and visited[x*2]==-1:
            visited[x*2] = visited[x]
            q.append(x*2)
        if (0<= x+1 <= 100000) and visited[x+1]==-1:
            visited[x+1] = visited[x]+1
            q.append(x+1)

bfs(n)

def dfs(start):
    stack = []
    stack.append(start)
    visited[start] = 0
    while stack:
        x = stack.pop()
        if x != k:
            dd = (x-1,x+1,x*2)
            for ddx in dd:
                if 0<=ddx<k*2 and visited[ddx] > visited[x]+1:
                    if ddx == dd[-1]:
                        visited[ddx] = visited[x]
                    else:
                        visited[ddx] = visited[x]+1
                    stack.append(ddx)
    return visited[k]
