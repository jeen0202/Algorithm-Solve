import sys
sys.stdin = open("Baekjoon/BruteForce/Tetromino/input.txt","r")
n,m = map(int,input().split())
p = [list(map(int,input().split())) for _ in range(n)]
dd = [(1,0),(-1,0),(0,1),(0,-1)]
visit = [[False for _ in range(m)]for _ in range(n)]
max_check = max(map(max,p))
ans = 0
def dfs(start,cnt,total):
    global ans
    x,y = start
    if total + max_check*(4-cnt) <= ans:
        return
    if cnt ==4:
        ans = max(ans,total)
        return
    else :
        for dx,dy in dd:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:                
                if cnt ==2:
                    visit[nx][ny] = True
                    dfs((x,y),cnt+1,total+p[nx][ny])
                    visit[nx][ny] = False
                visit[nx][ny] = True
                dfs((nx,ny),cnt+1,total+p[nx][ny])
                visit[nx][ny] = False

for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs((i,j),1,p[i][j])
        visit[i][j] = False
print(ans)

# def makeT(past,now):
#     global ans
#     x,y = now
#     temp = p[x][y]
#     for dx,dy in dd:
#         nx,ny = x+dx,y+dy
#         if 0<=nx<n and 0<=ny<m:
#             if (nx,ny) != past:
#                 temp+=p[nx][ny]
#     ans = max(ans,temp)