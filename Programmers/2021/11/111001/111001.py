import sys
import re
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(1)]

def solution(name):
    answer = 0
    min_move = len(name)-1
    
    for index,item in enumerate(name):
        print([ord(item)-65,91-ord(item)])        
        answer += min(ord(item)-65,91-ord(item))
        next = index+1
        while next <len(name) and name[next] == 'A':
            next+=1
            
        min_move = min(min_move,index+index +len(name)-next)
        print(min_move)
    answer += min_move
    return answer

if __name__ == '__main__':    
    print(solution(arr[0][0]))

