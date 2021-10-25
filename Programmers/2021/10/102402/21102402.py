import sys
import math
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(1)]

def solution(n):
    offset = ['4','1','2']
    answer = ''
    while n:
       answer = offset[n%3] + answer
       n = n//3 - (n%3==0)
       # 0이없는것을 반영
    return answer

if __name__ == '__main__':    
    print(solution(arr[0][0]))

