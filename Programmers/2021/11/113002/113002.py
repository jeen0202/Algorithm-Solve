def solution(number,k):
    answer = []
    for n in number :
        if not answer :
            answer.append(n)
            continue
        while answer and k >0 and answer[-1] < n:
            answer.pop()
            k -= 1
        answer.append(n)
    if k>0:
        return "".join(answer[:-k])    
    return "".join(answer)
if __name__ == '__main__':    
    print(solution("1924",2))
    print(solution("1231234",3))
    print(solution("4177252841",4))
    print(solution("99990",2))

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

    