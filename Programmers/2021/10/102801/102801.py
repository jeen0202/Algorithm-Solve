import sys
from collections import Counter
from itertools import combinations
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(2)]
arr[1] = list(map(int,arr[1]))

def solution(orders,course):    
    answer= []    
    for menu in course: 
        temp= []       
        for order in orders:
            comb = combinations(sorted(order),menu)
            temp+= comb
        sorted_temp = Counter(temp)
       	
        if sorted_temp:
            max_comb = max(list(sorted_temp.values()))
            if max_comb >=2:
                for key in sorted_temp.keys():
                    if sorted_temp[key] == max_comb:
                        answer.append("".join(key))    
    return sorted(answer)

if __name__ == '__main__':    
    print(solution(arr[0],arr[1]))
    #solution(arr[0],arr[1])

