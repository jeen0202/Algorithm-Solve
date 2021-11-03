import sys
import re
from itertools import permutations
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(expression):
    expression = str(expression)
#    num = re.finditer('[/*+-]',expression)
    orders = list(permutations(['*','+','-'],3))
    num = re.split('[*+-]',expression)
    num = list(map(int,num))
    max = 0
    
    #result = re.search(regex,expression)
    #print(result.group())
    for order in orders:
        temp_exp = expression
        for exp in order:
            regex = f"(\d+)\{exp}(\d+)|^-(\d+)\{exp}(\d+)"                        
            while re.search(regex,temp_exp):                   
                #regex = f"(\d+)\{exp}(\d+)|^-(\d+)\{exp}(\d+)"
                temp = re.search(regex,temp_exp).group()                                       
                temp_exp = temp_exp.replace(temp,str(eval(temp)),1)
        temp_exp = int(temp_exp)
        if temp_exp <0 :
            temp_exp *= -1
        if temp_exp > max :
            max = temp_exp
                          
    return max

if __name__ == '__main__':    
    print(solution(arr[0][0]))

