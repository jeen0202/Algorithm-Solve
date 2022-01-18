import sys
sys.stdin = open("Baekjoon/Graph/Tomato/input.txt","r")
M,N = map(int,input().split(" "))
Graph,visited = [],[]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
day = 0
for i in range(N):
    Graph.append(list(map(int,input().split(" "))))
for i in range(N):
    for j in range(M):
        if Graph[i][j] == 1:
            visited.append([i,j])
def doneCheck(visited):
    check = 0
    for line in Graph:
        check += line.count(0)
    if check == 0:
        return False
    return True
def OneDay(x,y,visited=visited,Graph=Graph):
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        check = [nx,ny]
        if nx <0 or nx >=N or ny <0 or ny >=M:
            continue
        if Graph[nx][ny] !=0 and check in visited:
            continue
        Graph[nx][ny]=1
        visited.append([nx,ny])
    return -1
while doneCheck(visited):
    for item in visited:        
        OneDay(item[0],item[1])
    for line in Graph:
        print(line)
    print()
    day+=1
print(day)