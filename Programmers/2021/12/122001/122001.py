def solution(numbers):
    answer = []
    for item in numbers: 
        temp = item        
        while True:
            temp +=1
            count = len(bin(temp))-len(bin(item))                   
            for i in range(1,len(bin(item))-1):
                if bin(item)[-i] != bin(temp)[-i]:
                    count+=1
            if count >2: 
                continue
            answer.append(temp)
            break
    return answer
if __name__ == '__main__':    
    print(solution([2,7]))

