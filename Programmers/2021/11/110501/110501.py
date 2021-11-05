
import sys
#sys.stdin = open(sys.argv[1],'r')
#arr  = [list(map(str,input().split())) for _ in range(1)]

# def getdirt(a) :
#     direction = {"x":[0,1],"-x":[0,-1],"y":[1,0],"-y":[-1,0]}
#     for key, value in direction.items():
#         if a == value:
#             dirt = key
#     return dirt
arrows = {
    "down":[1,0],
    "up":[-1,0],
    "right":[0,1],
    "left":[0,-1]} 
   
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
        temp[1] == temp[0]%2
    if temp[0] < 0:
        temp[0] = y_max-1
    if temp[1] < 0:
        temp[1] = x_max-1
    
    return now, temp, dirt
    
def solution(grid):
    answer=[]    
    first = [0,0]
    now = [1,0]        
    past = first    
    first_dirt = [now[i]-first[i] for i in range(len(now))] 
    print(f'fisrt : {past} {first_dirt}')
    past,now,dirt = getnext(now,first_dirt,grid)
    print(f"now : {past} {dirt}")
    index = 3     
    while True:        
       # dirt = [now[i]-past[i ] for i in range(len(now))]             
        past,now,dirt = getnext(now,dirt,grid)
        arrow =""
        print(dirt)  
        for key, value in arrows.items():
            if dirt == value:
                arrow = key
        print(f'now :{now} dirt : {dirt} arrorw: {arrow} {index}')
        if now == first and dirt == first_dirt:
            break;
        index +=1

         

        
        
    return answer
    


if __name__ == '__main__':    
    print(solution(["SL","LR"]))

