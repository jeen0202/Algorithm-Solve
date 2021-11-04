import sys
import re
from itertools import permutations
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(expression):
    expression = str(expression)
    orders = list(permutations(['*','+','-'],3))
    max = 0
    
    for order in orders:
        num = re.findall('[0-9]+',expression)
        ops = re.findall('[*+-]+',expression) 
         
        for exp in order:
            while exp in ops:
                index = ops.index(exp) 
                if str(eval(num[index]+exp+num[index+1])) != 0:             
                    num[index] =str(eval(num[index]+exp+num[index+1]))                                                   
                del num[index+1] 
                del ops[index]                                
        if abs(int(num[0]))> max:
            max = abs(int(num[0]))                          
    return max

if __name__ == '__main__':    
    print(solution(arr[0][0]))
