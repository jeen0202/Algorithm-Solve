import sys
from collections import deque
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(8)]
def DFS(graph, start,visited,result):
    visited[start] = True    
    result.append(start)
    for i in graph[start]:
        if not visited[i]:
            DFS(graph,i,visited,result)
    

def solution(graph): 
    visited = [False]*8
    result = []   
    DFS(graph,1,visited,result)
    return result

if __name__ == '__main__':    
    print(solution(arr))
