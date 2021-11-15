import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(3)]

def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()


if __name__ == '__main__':    
    print(solution(arr[0][0],arr[1][0],arr[2][0]))

