def solution(A):
    n = len(A)
    return sum(range(n+2)) - sum(A)

if __name__ == '__main__':    
    print(solution([2,3,1,5]))

