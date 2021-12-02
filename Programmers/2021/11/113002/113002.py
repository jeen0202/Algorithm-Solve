def solution(number,k):
    answer = []
    cnt = len(number)-k
    number = list(number)
    answer.append(number.pop(0))
    while number:
        print(answer)        
        top = len(answer)-1
        temp = number.pop(0)
        while len(answer) and int(answer[top]) < int(temp) and len(answer)+len(number)>=cnt:
            answer.pop()
            top -= 1
        answer.append(temp)
        
        
        
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
    # 에러
    # i = number.pop(0)
    # top = len(answer)
    # if cnt == len(number)+top:
    #     answer.append(i)            
    # else :       
    #     while len(answer) and int(answer[-1])-int(i) <0:
    #         answer.pop()
    #     if top > len(answer) or len(answer)<len(number)-k:
    #         answer.append(i)  

    