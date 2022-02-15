import sys
sys.stdin = open("Baekjoon/BruteForce/Tetromino/input.txt","r")
n,m = map(int,input().split())
p = [list(map(int,input().split())) for _ in range(n)]
dd = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[0 for _ in range(m)]for _ in range(n)]
ans = 0
def dfs(start,visit,cnt):
    global ans
    x,y = start
    visit[x][y] = p[x][y]
    if cnt == 2:
        temp = p[x][y]
        check =0
        for dx,dy in dd:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                temp += p[nx][ny]
                check+=1
        if check == 4:
            ans = max(ans,temp)
    if cnt <4:
        for dx,dy in dd:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<= ny<m:                
                visit[nx][ny] = visit[x][y]+p[nx][ny]
                if cnt+1 ==4:
                    ans = max(ans,visit[nx][ny])
                else:
                    dfs((nx,ny),visit,cnt+1)


for i in range(n):
    for j in range(m):
        dfs((i,j),visited,1)
print(ans)