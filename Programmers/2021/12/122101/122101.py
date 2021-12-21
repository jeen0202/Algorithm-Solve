from itertools import combinations_with_replacement as comb
def solution(n,money):
    max = n//money[0]
    hubo,answer = [],[]
    for i in range(1,max+1):
        hubo.extend(list(comb(money,i))) 
    #print(hubo)    
    answer=list(map(sum,hubo))
    #answer = [sum(tup) for tup in hubo]
    return answer.count(n)
        
if __name__ == '__main__':    
    print(solution(5,[1,2,5]))

