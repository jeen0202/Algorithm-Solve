
def solution(citations):
    citations.sort(reverse=True)    
    return max(map(min,enumerate(citations,start=1)))   
    

if __name__ == '__main__':    
    print(solution([3,0,6,1,3,5]))
    print(solution([0,0,0,0,1]))
    print(solution([12, 11, 10, 9, 8, 1]))
    print(solution([0,0,0]))
