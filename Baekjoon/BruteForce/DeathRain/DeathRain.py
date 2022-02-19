import sys
sys.stdin = open("Baekjoon/BruteForce/DeathRain/input.txt","r")
n,h,d = map(int,input().split())
maps = [list(input()) for _ in range(n)]
dd = [(-1,0),(1,0),(0,-1),(0,1)]
visited = [[0 for _ in range(n)]for _ in range(n)]

from collections import deque
def bfs(start): 
    q = deque()
    q.append(start)
    
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
                    th = d                    
                elif td > 0:
                    td -= 1
                else:
                    th -= 1
                if th <=0:
                    continue
                if visited[nx][ny] < th+td:
                    visited[nx][ny] = th+td
                    q.append((nx,ny,th,td,cnt+1))
    print(-1)
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'S':
            visited[i][j] = h
            bfs((i,j,h,0,0))

# sys.setrecursionlimit(10000)
# def avoidRain(start,nh,visit):
#     global ans,umbrellaCount
#     x,y = start
#     if  nh<= 0:
#         return
#     for dx,dy in dd:
#         nx,ny = x+dx,y+dy
#         if 0<=nx<n and 0<=ny<n and visit[nx][ny] ==-1:
#             if maps[nx][ny] == 'E':
#                 if ans == -1:
#                     ans = visited[x][y]+1
#                 else:
#                     ans = min(ans,visited[x][y]+1)
#                 return            
#             if maps[nx][ny] == 'U':
#                 umbrellaCount = d  
#             else:
#                 if umbrellaCount>0:
#                     umbrellaCount -=1
#                 else:
#                     nh -=1
#             visit[nx][ny] = visit[x][y]+1                
#             avoidRain((nx,ny),nh,visit)
#             visit[nx][ny] = -1
#             nh +=1
