import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(1)]
numbers = arr[0]

def f1(x):
    temp = x[:]
    while len(temp) < max_size:
        if temp[-1] == '0':
            temp += '1'
        else :temp+=temp[0]
    #print(temp)
    return temp
    
def solution(numbers):
    answer = ""
    split_numbers = (list(map(list,map(str,list(map(str,numbers))))))
    global max_size
    max_size = max(len(number) for number in split_numbers)
    
    sorted_numbers = sorted(split_numbers,key=f1,reverse=True)
    #print(sorted_numbers)

    for i in range(len(sorted_numbers)-1):
        a = str("".join(sorted_numbers[i]))
        b = str("".join(sorted_numbers[i+1]))
        if int(b+a) > int (a+b):
            sorted_numbers[i],sorted_numbers[i+1] = sorted_numbers[i+1],sorted_numbers[i]
    for number in sorted_numbers:
        answer += "".join(number)
    if all(element == '0' for element in answer):
        answer = '0'
    return answer

if __name__ == '__main__':    
    print(solution(numbers))

