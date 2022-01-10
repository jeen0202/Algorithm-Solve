def solution(A,B,K):
    return B//K - (A//K -(A%K==0))

if __name__ == '__main__':    
    print(solution(6,11,2))

