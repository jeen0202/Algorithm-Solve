import sys
from collections import deque
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(8)]
def BFS(graph, start,visited):    
    queue = deque([start])
    visited[start] = True
    result = []
    while queue:
        n = queue.popleft()
        result.append(n)
        for i in graph[n]:
            if not visited[i]:                
                queue.append(i)
                visited[i] = True    
    return result
def solution(graph): 
    visited = [False]*8   
    return(BFS(graph,1,visited))

if __name__ == '__main__':    
    print(solution(arr))
