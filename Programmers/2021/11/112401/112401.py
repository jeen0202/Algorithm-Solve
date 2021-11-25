# import sys
# sys.stdin = open(sys.argv[1],'r')
# arr  = [list(map(list,input().split())) for _ in range(3)]
import heapq

def dijkstra(graph,max):
    distances = {node: float('inf') for node in graph}
    distances[1] = 0
    queue = []
    answer = 0
    heapq.heappush(queue,[distances[1],1])
    
    while queue:
        current_dis, current_des = heapq.heappop(queue)
        
        if distances[current_des] < current_dis:
            continue
        for new_des, new_dis in graph[current_des].items():
            distance = current_dis+ new_dis
            if distance < distances[new_des]:
                distances[new_des] = distance
                heapq.heappush(queue,[distance, new_des])
    for item in distances.values():
        if item <= max:
            answer +=1
    print(distances)
    return answer

def solution(N,road,K):    
    graph = {}    
    temp = [{}for _ in range(N+1)]
    while road:
        w = road.pop(0)
        point1,point2,time = w
        if point1 in temp[point2].keys() or point2 in temp[point1].keys():
            temp[point1][point2] = min([temp[point1][point2],time])
            temp[point2][point1] = min([temp[point2][point1],time])
        else :
            temp[point1][point2] = time
            temp[point2][point1] = time
    #print(temp)
    for index,item in enumerate(temp):
        if index!=0:                    
            graph[index] = item  
    #print(graph)  
    return dijkstra(graph,K)

if __name__ == '__main__':    
    print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
    print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))


