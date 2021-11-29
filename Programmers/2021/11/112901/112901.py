
def solution(citations):
    #citations = sorted(citations,reverse=True)
    # for index,item in enumerate(citations):
    #         if index+1 >= item:
    #             return item
    temp = sorted(sorted(set(citations),key = lambda x : citations.index(x)),reverse=True)   
    count = 0 
    print(temp)
    if temp[0] == 0:
        return 0    
    for index in range(temp[0],0,-1):             
        count += citations.count(index)       
        if count >= index:
            return index
            

if __name__ == '__main__':    
    print(solution([3,0,6,1,3,5]))
    print(solution([0,0,0,0,1]))
    print(solution([12, 11, 10, 9, 8, 1]))
    print(solution([0,0,0]))

