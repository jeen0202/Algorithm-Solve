from itertools import combinations
import time
def solution(number,k):    
    #start = time.time()
    answer = ['0']
    cnt = len(number)-k
    print(cnt)
    number = list(number)
    while number:
        i = number.pop(0)
        top = len(answer)
        if len(answer) < cnt:
            answer.append(i)            
        else :       
            while len(answer) and int(answer[-1])-int(i) <0:
                answer.pop()
            if top > len(answer) or len(answer)<len(number)-k:
                answer.append(i)
       
           
            
    #print(time.time()-start)         
    return "".join(answer)
if __name__ == '__main__':    
    print(solution("1924",2))
    print(solution("1231234",3))
    print(solution("4177252841",4))

    # 시간초과 2   
    # temp = list(map(int,map("".join,combinations(number,len(number)-k))))
    # f"{max(temp)}"
    # 시간초과 3
    # temp = list(map(int,map("".join,combinations(number,len(number)-k))))
    # temp.sort(reverse=True)
    # return f"{temp[0]}"
    # 시간초과 3

    