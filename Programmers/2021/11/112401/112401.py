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
    temp = [{}for row in range(N)]
    #for w in road:
    while road:
        w = road.pop(0)
        points = w[:-1]
        time = w[-1]
        if max(points) in temp[min(points)-1].keys():            
            temp[min(points)-1][max(points)]=min([temp[min(points)-1][max(points)],time])
        else :
            temp[min(points)-1][max(points)]=time
    print(temp)
    for index,item in enumerate(temp,1):                    
        graph[index] = item    
    return dijkstra(graph,K)

if __name__ == '__main__':    
    print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
    print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))


