from collections import deque
queue = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(maps,visited):
    queue = deque([(0,0,1)])
    visited[0][0] = 1
    while queue:
        cur = queue.popleft() 
        #print(cur)
        if cur[0] ==n and cur[1] == m:
           # for line in visited:
               # print(line)
            return cur[2]
        for i in range(4):                        
            xx= dx[i] + cur[0]
            yy= dy[i] + cur[1]
            
            #print(xx,yy,visited[xx][yy],maps[xx][yy])            
            if 0<=xx<=n and 0<=yy<=m and visited[xx][yy] ==0 and maps[xx][yy] ==1:                                 
                visited[xx][yy] = 1
                queue.append([xx,yy,cur[2]+1])
    return -1           
def solution(maps):
    global n,m
    n,m = len(maps)-1, len(maps[0])-1
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    if maps[n-1][m] == 0 and maps[n][m-1] ==0:
        return -1
    return bfs(maps,visited)
    

if __name__ == '__main__':    
    print(solution([
[1,0,1,1,1],
[1,0,1,0,1],
[1,0,1,1,1],
[1,1,1,0,1],
[0,0,0,0,1]
]))

