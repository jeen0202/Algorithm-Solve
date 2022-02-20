import sys
sys.stdin = open("Baekjoon/BruteForce/DeathRain/input.txt","r")
n,h,d = map(int,input().split())
maps = [list(input()) for _ in range(n)]
dd = [(-1,0),(1,0),(0,-1),(0,1)]

from collections import deque
def bfs(start): 
    visited = [[0]*n for _ in range(n)]
    visited[start[0]][start[1]] = h
    q = deque([start])
    
    while q:
        x,y,nh,nd,cnt =q.popleft()
        for dx,dy in dd:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                if maps[nx][ny] == 'E':
                    print(cnt+1)
                    return          
                th,td = nh,nd
                if maps[nx][ny] == 'U':
                    td = d                    
                if td > 0:
                    td -=1
                else:
                    th -=1
                if th == 0 :
                    continue
                if visited[nx][ny] < th:
                    visited[nx][ny] = th
                    q.append((nx,ny,th,td,cnt+1))
    print(-1)
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'S':            
            bfs((i,j,h,0,0))