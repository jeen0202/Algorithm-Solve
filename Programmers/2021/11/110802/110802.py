import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(1)]
numbers = arr[0]
max_size = 4
def f1(x):
    temp = x[:]
    while len(temp) < max_size:
        if temp[-1] == '0':
            temp += '1'
        else :temp+=temp[0]
    return temp
    
def solution(numbers):
    answer = ""
    if all(element == 0 for element in numbers):
        return '0'
    split_numbers = map(str,list(map(str,numbers)))
    sorted_numbers = sorted(split_numbers,key=f1,reverse=True)
    i = 0
    while i< len(sorted_numbers)-1:    
        a = str("".join(sorted_numbers[i]))
        b = str("".join(sorted_numbers[i+1]))
        if int(b+a) > int (a+b):
            sorted_numbers[i],sorted_numbers[i+1] = sorted_numbers[i+1],sorted_numbers[i]
            i -= 1
            if i <0:
                i =0
            continue
        i+=1
    for number in sorted_numbers:
        answer += "".join(number)
    return answer

if __name__ == '__main__':    
    print(solution(numbers))

