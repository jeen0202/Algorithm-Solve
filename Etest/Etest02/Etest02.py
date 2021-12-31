from collections import deque
def solution(stones, k):
    visited = [0]*len(stones)
    game = [-1]*len(stones)
    queue = deque()
    queue.append([0,0])
    def bfs(stones,visited,k):
        queue.append(stones)
        while queue:
            temp = queue.popleft()            
            for i in range(len(temp)):
                mtemp=[]
                for i in range(len(temp)):
                    mtemp.append(temp[i]-game[i])
                mtemp[i] +=2
                print(mtemp)
                if -1 in mtemp or mtemp.count(0)>1 or mtemp.count(k)>2:
                    continue
                if mtemp[i] != k or sum(mtemp)!=k:
                    visited[i] +=1
                    queue.append(mtemp)
                else: 
                    return
    bfs(stones,visited,k)   
    return visited
if __name__ == '__main__':    
    print(solution([1, 3, 2],3))

