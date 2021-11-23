import sys
sys.stdin = open(sys.argv[1],'r')
arr  = input()

from collections import deque
code = {"[":"]","{":"}","(":")"}

def solution(s):
    if len(s) == 0 or len(s)%2 != 0:
        return 0
    keys = list(code.keys())
    answer=  0
        
    for index in range(len(s)):       
        temp = deque(list(s))
        temp.rotate(-index)              
        while len(temp)>0:
            x = temp.popleft()            
            if x not in keys or code[x] not in temp:
                break
            elif temp[0] in keys and temp[temp.index(code[x])-1] not in ["]","}",")"]:
                break               
            else:
                temp.remove(code[x])                
                if len(temp) %2 != 0 :
                    break;
            if len(temp) == 0:
                answer +=1            
    return answer

if __name__ == '__main__':    
    print(solution(arr))

