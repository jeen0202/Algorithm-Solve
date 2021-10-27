import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(2)]
arr[1] = list(map(int,arr[1]))

def solution(orders,course):
    return orders, course

if __name__ == '__main__':    
    print(solution(arr[0],arr[1]))

