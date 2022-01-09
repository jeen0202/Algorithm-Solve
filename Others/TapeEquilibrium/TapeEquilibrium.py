def solution(A):
    N = len(A)
    P = [0] * (N)
    sumA = sum(A)-A[0]
    if N==2:
        return abs(A[0]-A[1])
    P[0] = abs(A[0] - sumA)
    sumA -= A[1]
    A[1] += A[0]
    P[1] = abs(A[1] - sumA)
    for i in range(2,N):
        sumA -=A[i]
        A[i] +=A[i-1]
        P[i] = abs(A[i] - sumA)    
    return min(P[:-1])
if __name__ == '__main__':    
    print(solution([3,1,2,4,3]))
    print(solution([-2,-3,-4,-1])) #0

