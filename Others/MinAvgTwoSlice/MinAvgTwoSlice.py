def solution(A):
    minAvg =(A[1] + A[0])/2
    minIndex = 0
    for i in range(2,len(A)):
        temp = (A[i] + A[i-1] + A[i-2])/3
        if minAvg > temp:
            minAvg = temp
            minIndex = i-2
        temp = (A[i] + A[i-1])/2
        if minAvg > temp:
            minAvg = temp
            minIndex = i-1
    return minIndex
if __name__ == '__main__':    
    print(solution([4,2,2,5,1,5,8]))

