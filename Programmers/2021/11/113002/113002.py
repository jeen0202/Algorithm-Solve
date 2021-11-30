from itertools import combinations

def solution(number,k):
    answer = 0
    temp = list(combinations(number,len(number)-k))
    
    for item in temp:
        str = "".join(item)
        if int(str) > answer:
            answer = int(str)        
    return f"{answer}"

if __name__ == '__main__':    
    print(solution("1924",2))
    #print(solution("1231234",3))
    #print(solution("4177252841",4))

