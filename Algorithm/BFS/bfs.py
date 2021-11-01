import sys
from collections import deque
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(3)]
arr = map(int,arr)
def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

def solution(graph):
    return(BFS(graph,1))

if __name__ == '__main__':    
    print(solution(arr))
