def solution(A):
    mInt = 1
    A.sort()
    for item in A:
        if item == mInt:
            mInt+=1
    return mInt
if __name__ == '__main__':    
    print(solution([1,3,6,4,1,2]))
    print(solution([1,2,3]))
    print(solution([-1,-3]))

