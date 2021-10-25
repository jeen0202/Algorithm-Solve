import sys
sys.stdin = open(sys.argv[1],"r")
arr  = [list(map(int,input().split())) for _ in range(2)]

def solution(lottos, win_nums):
    answer = []
    best= 7
    worst = 7
    unknown = 0
    
    for lotto in lottos:
        for win_num in win_nums:
            if lotto == win_num:
                best-=1
                worst-=1
        if lotto == 0:
        	unknown+=1
    if best-unknown == 7:
        answer.append(6)
    else:
    	answer.append((best-unknown))
    if worst == 7:
        answer.append(6)
    else:
    	answer.append(worst)
    return answer

if __name__ == "__main__":
    print(solution(arr[0],arr[1]))

