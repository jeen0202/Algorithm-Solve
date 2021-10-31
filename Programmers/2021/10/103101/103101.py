import sys
from collections import deque
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(5)]
mx = [1,0,-1,0]
my = [0,-1,0,1]
def BFS(person,x,y):
    visited = [[0,0,0,0,0] for x in range(5)]
    queue = deque()
    queue.append([x,y,0])
    visited[x][y] = 1
    
    while queue :
        n = queue.popleft()
        if 1 <= n[2] <= 2 and person[n[0]][n[1]] == "P":
            return 0
        if n[2] >= 3:
            break;
        for m in range(4):
            next = [0,0,0]
            next[0] = n[0] + mx[m]
            next[1] = n[1] + my[m]
            next[2] = n[2] +1
            
            if 0 <= next[0] < 5 and 0 <= next[1] < 5:
                if person[next[0]][next[1]] != "X" and visited[next[0]][next[1]] == 0:
                    queue.append(next)
                    visited[next[0]][next[1]] = 1
    return 1

#  맨해튼 거리 = |r1 - r2| + |c1 - c2|
def solution(places):
    answer = []
       
    for place in places:
        check = True        
        for row in range(5): 
            for columns in range(5):
                if place[row][columns] == "P":
                    if BFS(place,row,columns)==0:
                        check = False
                        break
            if check == False:
                break
        if check == False:
            answer.append(0)
        else : answer.append(1)            
        # if len(person) <=1:
        #     answer.append(1)    
        # else :
        #     print(person)
        #     check = 1              
        #     for i in range(len(person)):                              
        #         for j in range(i+1,len(person)):
        #             x1,y1 = person[i][0], person[i][1]
        #             x2,y2 = person[j][0], person[j][1]
        #             mht = math.fabs(x1 - x2)+math.fabs(y1 - y2)
        #             if mht <= 2:
        #                 #print(x1,y1,x2,y2)
        #                 #print(place[x1][y1], place[x2][y2])                        
        #                 if x1==x2 and place[x1][y1+1]!= "X":
        #                     #print(x1,y1,place[x1][y1+1])
        #                     check = 0
        #                 elif y1==y2 and place[x1+1][y1]!= "X":
        #                     #print(x1,y1,x2,y2, place[x1+1][y1])
        #                     check = 0
        #                 elif x1==y2 and x2==y1 and (place[x1][y2] != "X" or place[x2][y1] != "X"):
        #                     #print(x1,y1,x2,y2,place[x1][y2],place[x2][y1])
        #                     check = 0
        #     answer.append(check)
    return answer    
                
            
if __name__ == '__main__':    
    print(solution(arr))

