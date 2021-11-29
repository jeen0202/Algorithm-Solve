
def solution(citations):
    #citations = sorted(citations,reverse=True)
    # for index,item in enumerate(citations):
    #         if index+1 >= item:
    #             return item
    temp = sorted(sorted(set(citations),key = lambda x : citations.index(x)),reverse=True)    
    print(citations)
    count = 0 
    for item in temp:
        count += citations.count(item)
        if count >= item:            
            return item
            

if __name__ == '__main__':    
    print(solution([3, 0, 6, 1, 5]))

