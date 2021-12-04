from collections import deque

def bfs(dungeons,start,k):
    queue = deque([start])    
    visited =[0 for _ in range(len(dungeons))]
    if dungeons[start][0]>k:
        return 0
    visited[start] = True
    k -= dungeons[start][1]
    result = 1
    while queue:
        n = queue.popleft()
        result+=1
        for i,d in enumerate(dungeons):
            if not visited[i] and d[0]<k:
                k-=d[1]
                queue.append(i)
                visited[i] = True
    return result
def solution(k,dungeons):
    answer = []
    dungeons.sort(key=lambda x : x[0],reverse=True)
    for dungeon in dungeons:
        answer.append(bfs(dungeons,dungeons.index(dungeon),k))  
    return max(answer)        

if __name__ == '__main__':    
    print(solution(80,[[80,20],[50,40],[30,10]]))

#1차 실패
    # while True:
    #     flag = answer
    #     next = [9,k]
    #     for dungeon in dungeons:
    #         if dungeon[0] <= k and dungeon[1] < next[1]:
    #             next = [dungeons.index(dungeon),dungeon[1]]
    #     if next[0]<=8 and next[1] != k:
    #         print(next)            
    #         dungeons.pop(next[0])
    #         k-=next[1]             
    #         answer +=1
    #     else:
    #         break 