from collections import deque
queue = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,board,visited):
    queue = deque([x,y,0])
    visited[x][y] = True
    while queue:
        cur = queue.popleft()
        if cur[0] ==n-1 and cur[1] == m-1:
            print(cur[2])
            return
        for i in range(4):
            xx= dx[i] + cur[0]
            yy= dy[i] + cur[1]
            if 0<=xx<n and 0<=yy<m and not visited[xx][yy] and board[xx][yy] == 1:
                visited[xx][yy] = True
                queue.append((xx,yy,cur[2]+1))
def solution(maps):
    global n,m
    n,m = len(maps)-1, len(maps[0])-1
    visited = [[0]*m] for _ in range(0,n)]
    print(visited)
    n,m= len(maps)-1, len(maps[0])-1
    if maps[n-1][m] == 0 and maps[n][m-1] ==0:
        return -1


if __name__ == '__main__':    
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

