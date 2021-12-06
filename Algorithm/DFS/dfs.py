#Graph 는 1부터 시작하는 요소 7개의 완전이진트리
import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(8)]

def DFS(graph, start,visited,result):
    visited[start] = True    
    result.append(start)
    for i in graph[start]:
        if not visited[i]:
            DFS(graph,i,visited,result)

def DFS_Stack(graph,start):
    visited = list()
    stack = list()    
    # Stack 최초값 입력
    stack.append(start)    
    while stack:
        node = stack.pop()
        # 조건부분
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
        print(f"stack : {stack}\nvisited : {visited}")
    return visited

# set의 경우 graph는 key-value형식이고 value는 set형식이여야한다.
def DFS_set(graph,start,visited=None):
    result=[]
    if visited is None:
        visited = set()
    visited.add(start)
    result.append(start)
    print(start)
    for next in graph[start] - visited:
        DFS_set(graph,next,visited)
    return visited

def solution(graph): 
    visited = [False]*8
    result = []   
    #DFS(graph,1,visited,result)
    #DFS_Stack(graph,1)
    #DFS_set(graph,1)
    return result

if __name__ == '__main__':    
    print(solution(arr))
