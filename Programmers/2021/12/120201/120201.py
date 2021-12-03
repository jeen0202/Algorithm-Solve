def solution(k,dungeons):
    answer = 1
    dungeons.sort(key=lambda x : x[0],reverse=True)
    while True:
        flag = answer
        next = [9,k]
        for dungeon in dungeons:
            if dungeon[0] <= k and dungeon[1] < next[1]:
                next = [dungeons.index(dungeon),dungeon[1]]
        if next[0]<=8 and next[1] != k:            
            dungeons.pop(next[0])
            k-=next[1] 
            answer +=1
        else:
            break   
    return answer        

if __name__ == '__main__':    
    print(solution(80,[[80,20],[50,40],[30,10]]))

