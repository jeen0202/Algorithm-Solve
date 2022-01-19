import sys
sys.stdin = open("Baekjoon/Graph/Tomato/input.txt","r")
M,N = map(int,input().split(" "))
Graph,visited = [],[]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
remain = M*N
day = 1
for i in range(N):
    Graph.append(list(map(int,input().split(" "))))
    remain-= Graph[i].count(-1)
for i in range(N):
    for j in range(M):
        if Graph[i][j] == 1:
            remain -=1
            visited.append([i,j])
def OneDay(x,y,day,visited=visited,Graph=Graph):
    newT = 0
    day+=1
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        check = [nx,ny]
        if nx <0 or nx >=N or ny <0 or ny >=M:
            continue
        if Graph[nx][ny] !=0 or check in visited:
            continue
        Graph[nx][ny]+=day
        newT+=1
        visited.append([nx,ny])
    return newT
newT = 0
while True:
    if remain == 0:
        print(0)
        break
    for x,y in visited:
        if Graph[x][y] == day:
            newT += OneDay(x,y,day)
    day+=1
    if remain == newT:
        print(day-1)
        break
    if newT == 0:
        print(-1)
        break

