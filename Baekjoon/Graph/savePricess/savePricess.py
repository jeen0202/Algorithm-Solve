import sys
sys.stdin = open("Baekjoon/Graph/savePricess/input.txt","r")
from collections import deque
N,M,T = map(int,input().split(" "))
p = []
dd = [(-1,0),(1,0),(0,-1),(0,1)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
for i in range(N):
    p.append(list(map(int,input().split(" "))))
    for j in range(M):
        if p[i][j] == 2:
            sx,sy= (i,j)
ads = N+M-sx-sy-2
# 검에 도달한 후 직선거리와 검을 배제한 최단거리 비교(BFS)
q = deque()
q.append((0,0))
visited[0][0] = 0
while q:
    x,y = q.popleft()
    for i in range(4):
        dx,dy = (sum(e) for e in zip(dd[i],(x,y)))
        if 0<=dx<N and 0<=dy<M and visited[dx][dy] == -1:
            if p[dx][dy] != 1:
                visited[dx][dy] = visited[x][y] +1
                q.append((dx,dy))
# 조건에 따른 ans
if visited[N-1][M-1] == -1:
    if visited[sx][sy] == -1:
        print("Fail")
        exit()
    else:
        ans = visited[sx][sy] + ads
elif visited[sx][sy] == -1:
    ans = visited[N-1][M-1]
else:
    ans = min(visited[N-1][M-1],ads+visited[sx][sy])
print(ans) if ans <= T else print("Fail")
exit()