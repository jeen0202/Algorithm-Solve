import sys
import math

sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(1)]

def solution(w,h):
    gcd = math.gcd(w,h)
    answer = w*h - (w + h - gcd)
  
    return answer

if __name__ == '__main__':    
    print(solution(arr[0][0],arr[0][1]))

