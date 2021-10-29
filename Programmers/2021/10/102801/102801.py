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
    count_pair = {}
    answer = []
    for item in counter:        
        value = {}
        values = 0
        for string in orders:                
                values += string.count(item)
                if item in string:
                    for c in string:
                        if item != c:                            
                            if c in value:
                                value[c] += string.count(c)  
                            else : value[c]=1
        count[item] = values
        value = sorted(value.items(),key=lambda x:x[1], reverse=True)
        count_pair[item]=value
        #print(value)
    # for item in count_pair:
    #     print(item,count_pair[item])
    count= sorted(count.items(),key=lambda x: x[1],reverse=True)
    #print(count)
    for index in course:
        temp = ""
        temp += count[0][0]
        #for j in range(index-1):
            
                        
                    
    return answer

if __name__ == '__main__':    
    print(solution(arr[0],arr[1]))
    #solution(arr[0],arr[1])

