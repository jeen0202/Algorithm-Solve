import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(1)]
numbers = arr[0]

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
    


if __name__ == '__main__':    
    print(solution(numbers))

