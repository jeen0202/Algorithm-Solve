
def solution(n,money):
    # max = n//money[0]
    # hubo,answer = [],[]
    # dp_M = [0]*max    
    # for i in range(1,max+1):
    #     hubo.extend(list(comb(money,i))) 
    # print(hubo)    
    # answer=list(map(sum,hubo))
    # answer = [sum(tup) for tup in hubo]
    # return answer.count(n)
    memo = [0] * (n+1)
    memo[0]=1
    for coin in money:
        for price in range(coin,n+1):            
            memo[price] += memo[price-coin]
    answer = memo[n] % 10000000007
    return answer
    
        
if __name__ == '__main__':    
    print(solution(5,[1,2,5]))

