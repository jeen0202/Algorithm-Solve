
import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]
dirt = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}

def DFS(location,org,route,grid,visited,answer):
    x = location[0]
    y = location[1]
    d = location[2]
    visited[d][x][y] = True
    
    now_x,now_y = x+dirt[d][1],y+dirt[d][0]
    
    if now_x >= len(grid):
        now_x = 0
    elif now_x < 0 :
        now_x = len(grid)-1
    if now_y >= len(grid[0]):
        now_y = 0
    elif now_y < 0 :
        now_y = len(grid[0])-1
    v = grid[now_x][now_y]    

    if v == 'R':
        d = (d + 5) % 4
        
    elif v == 'L':
        d = (d + 7) % 4
    if org == [now_x,now_y,d]:
        answer.append(route)
        return

    if not visited[d][now_x][now_y]:
        DFS([now_x,now_y,d],org,route+1,grid,visited,answer)
    

def solution(grid):
    visited = [[[0]*len(grid[0])for _ in range(len(grid))] for _ in range(4)]
    answer = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                DFS([i,j,d],[i,j,d],1,grid,visited,answer)
    return sorted(answer)


if __name__ == '__main__':    
    print(solution(arr[0]))

