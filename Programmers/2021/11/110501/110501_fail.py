
import sys
#sys.stdin = open(sys.argv[1],'r')
#arr  = [list(map(str,input().split())) for _ in range(1)]

# def getdirt(a) :
#     direction = {"x":[0,1],"-x":[0,-1],"y":[1,0],"-y":[-1,0]}
#     for key, value in direction.items():
#         if a == value:
#             dirt = key
#     return dirt
arrows = [
[1,0],
[-1,0],
[0,1],
[0,-1]]
   
def getnext(now,dirt,grid):    
    x_max = len(grid)
    y_max = len(grid[0])
    #print(f"dirt : {dirt} grid : {now}")        
    if grid[now[0]][now[1]] == "L":
        if dirt[0] == 0:
            dirt.reverse()
            dirt = [x*y for x,y in zip(dirt,[-1,-1])]
        else :
             dirt.reverse()
    elif grid[now[0]][now[1]] == "R":
        if dirt[0] == 0:
            dirt.reverse()
        else :
            dirt.reverse()
            dirt = [x*y for x,y in zip(dirt,[-1,-1])]
    #print(dirt,grid[now[0]][now[1]])        
    temp = [(now[i]+dirt[i]) for i in range(len(dirt))]   
    if temp[0] == y_max:
        temp[0] = temp[0]%2
    if temp[1] == x_max:
        temp[1] = temp[1]%2
    if temp[0] < 0:
        temp[0] = y_max-1
    if temp[1] < 0:
        temp[1] = x_max-1
    return temp, dirt
    
def solution(grid):
    answer=[]    
    first = [0,0]
    if len(grid)==1:
        if len(grid[0])==1:
            return[1,1,1,1]
    for first_dirt in arrows:                
        print(f'first : {first} first_dirt : {first_dirt}')
        now,dirt = getnext(first,first_dirt[:],grid)
        index = 1    
        while True:        
        # dirt = [now[i]-past[i ] for i in range(len(now))]             
            now,dirt = getnext(now,dirt,grid)
            index +=1
            print(f'now :{now} dirt : {dirt}') 
            if now == first and dirt == first_dirt:
                answer.append(index)
                break;
    return answer.sort()
    


if __name__ == '__main__':    
    print(solution(["S"]))

