import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(3)]
import math

def solution(N,A,B):
    answer = 0
    while N >1:
        answer +=1
        N /=2
        A = math.ceil(A/2)
        B = math.ceil(B/2)
        if A==B:
            return answer


if __name__ == '__main__':    
    print(solution(arr[0][0],arr[1][0],arr[2][0]))

