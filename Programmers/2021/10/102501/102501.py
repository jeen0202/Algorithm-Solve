import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(2)]

def solution(progresses, speeds):
    answer = []
    work_done = 0;
    works = progresses
    temp = 0      
    while work_done != len(progresses):
        for i in range(len(progresses)):            
            if works[i] < 100:
                works[i] += + speeds[i]
            else:
                if work_done == i:
                    work_done+=1
                    temp +=1                    
        if temp >0:
            answer.append(temp)
            temp = 0

    return answer
1
if __name__ == '__main__':    
    print(solution(arr[0],arr[1]))

