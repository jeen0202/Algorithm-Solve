import sys
sys.stdin = open("Baekjoon/BruteForce/DeathRain/input.txt","r")
n,h,d = map(int,input().split())
maps = [list(input()) for _ in range(n)]
print(maps)
dd = [(-1,0),(1,0),(0,-1),(0,1)]
visited = [[-1 for _ in range(n)]for _ in range(n)]
ans = -1
umbrellaCount = 0
def avoidRain(start,nh,visit):
    global ans,umbrellaCount
    x,y = start
    if  nh<= 0:
        return
    for dx,dy in dd:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and visit[nx][ny] ==-1:
            if maps[nx][ny] == 'E':
                if ans == -1:
                    ans = visited[x][y]+1
                else:
                    ans = min(ans,visited[x][y]+1)
                return            
            if maps[nx][ny] == 'U':
                umbrellaCount = d  
            else:
                if umbrellaCount>0:
                    umbrellaCount -=1
                else:
                    nh -=1
            visit[nx][ny] = visit[x][y]+1                
            avoidRain((nx,ny),nh,visit)
            visit[nx][ny] = -1
            nh +=1
sys.setrecursionlimit(10000)
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'S':
            visited[i][j] = 0
            avoidRain((i,j),h,visited)
print(ans)