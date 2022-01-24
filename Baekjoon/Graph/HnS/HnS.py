import sys
sys.stdin = open("Baekjoon/Graph/HnS/input.txt","r")
from collections import deque
n,k = map(int,input().split(" "))
visited = [False for _ in range(100001)]

def bfs(start):
    q = deque()
    q.append(start)
    visited[start[0]] = True
    while q:
        x,d = q.popleft()
        if x == k :
            break
        else :
            if (0<= x*2 < 100000) and visited[x*2]==False:
                visited[x*2] = True
                q.append((x*2,d))
            if (0<= x+1 < 100000) and visited[x+1]==False:
                visited[x+1] = True
                q.append((x+1,d+1))
            if (0<= x-1 < 100000) and visited[x-1]==False:
                visited[x-1] = True
                q.append((x-1,d+1))
    return d
print(bfs((n,0)))

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
