def solution(numbers):
    answer = []
    for item in numbers: 
        temp = item
        array = []
        while True:
            temp +=1
            count = len(bin(temp))-len(bin(item))
            if count >2: break
            #print(bin(temp)[2:])           
            for i in range(1,len(bin(item))-1):
                if bin(item)[-i] != bin(temp)[-i]:
                    count+=1
            if count >2: 
                continue
            array.append(temp)
        #print(answer)
        #print(min(answer))
        answer.append(min(array))
    return answer
if __name__ == '__main__':    
    print(solution([2,7]))

