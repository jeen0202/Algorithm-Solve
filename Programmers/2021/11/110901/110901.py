import sys
from itertools import permutations
import math
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(numbers):
    answer = 0
    numbers_list = []
    for item in numbers:
        numbers_list.append(item)
    le = len(numbers)    
    for i in range(2,le+1):
        for item in list(permutations(numbers,i)): 
            temp = ''.join(item)        
            numbers_list.append(temp)
    numbers_list = list(set(map(int,numbers_list)))        
   
    for number in numbers_list:        
        check = True
        if number in (0,1):
            check = False
        else:
            for i in range(2,int(math.sqrt(number))+1):
                if number%i == 0:                
                    check = False
            if check == True:                
                answer+=1
        
    return answer


if __name__ == '__main__':    
    print(solution(arr[0][0]))

