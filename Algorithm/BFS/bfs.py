import sys
from collections import deque
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(8)]
def BFS(graph, start):    
    queue = deque([start])
    visited=set()
    visited.add(start)
    result=[]
    while queue:
        n = queue.popleft()
        result.append(n)
        for i in graph[n]:
            if i not in visited:                
                queue.append(i)
                visited.add(i)
        print(queue)
        print(visited)
    return result

def BFS_Queue(graph,start):
    visit=list()
    queue=list()
    
    queue.append(start)
    
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
            print(f"queue : {queue}\nvisit : {visit}")
            
def solution(graph):       
    #return(BFS_Queue(graph,1))
    return(BFS(graph,1))

if __name__ == '__main__':    
    print(solution(arr))
