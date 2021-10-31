import sys
import math
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(5)]

#  맨해튼 거리 = |r1 - r2| + |c1 - c2|
def solution(places):
    answer = []    
    for place in places:
        person = []
        for row,columns in zip(place,range(len(place))):
            index = -1
            while True:
                index = row.find('P',index+1)
                if index == -1:
                    break;
                else :
                    person.append([columns,index])
        if len(person) <=1:
            answer.append(1)    
        else :
            print(person)
            check = 1              
            for i in range(len(person)):                              
                for j in range(i+1,len(person)):
                    x1,y1 = person[i][0], person[i][1]
                    x2,y2 = person[j][0], person[j][1]
                    mht = math.fabs(x1 - x2)+math.fabs(y1 - y2)
                    if mht <= 2:
                        #print(x1,y1,x2,y2)
                        #print(place[x1][y1], place[x2][y2])                        
                        if x1==x2 and place[x1][y1+1]!= "X":
                            #print(x1,y1,place[x1][y1+1])
                            check = 0
                        elif y1==y2 and place[x1+1][y1]!= "X":
                            #print(x1,y1,x2,y2, place[x1+1][y1])
                            check = 0
                        elif x1==y2 and x2==y1 and (place[x1][y2] != "X" or place[x2][y1] != "X"):
                            #print(x1,y1,x2,y2,place[x1][y2],place[x2][y1])
                            check = 0
            answer.append(check)
    return answer    
                
            
if __name__ == '__main__':    
    print(solution(arr))

