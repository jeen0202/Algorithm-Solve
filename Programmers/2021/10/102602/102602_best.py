import sys
import re
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(s): 
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return not(answer)
            


if __name__ == '__main__':    
    print(solution(arr[0][0]))

