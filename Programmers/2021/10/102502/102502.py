import sys
import heapq
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(2)]

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0    
    while scoville[0] < K:              
        if len(scoville) <2:
            answer = -1
            break
        heapq.heappush(scoville,heapq.heappop(scoville) +heapq.heappop(scoville)*2)
        answer+=1      
    return answer

if __name__ == '__main__':    
    print(solution(arr[0],arr[1][0]))
    
# 효율성 문제 해결1 (실패)
        # a = min(scoville)
        # scoville.pop(scoville.index(a))
        # b = min(scoville)
        # scoville.pop(scoville.index(b))
        # scoville.insert(a+b*2)
# 효율성 문제 해결2
    # heapq로 변환
