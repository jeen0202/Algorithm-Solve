import sys
from collections import Counter

sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(2)]
arr[1] = list(map(int,arr[1]))

def solution(orders,course):    
    counter = set()
    for item in orders:
        for j in item:
            counter.add(j)
    counter= sorted(counter)
    count = {} 
    print(counter)
    print("==============")
    answer = []
    for item in counter:
        print(orders.count(item))
        #count.update(item=orders.count(item))
            
                        
                    
    return count 

if __name__ == '__main__':    
    print(solution(arr[0],arr[1]))

