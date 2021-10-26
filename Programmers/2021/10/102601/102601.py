import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(int,input().split())) for _ in range(2)]


def solution(numbers, target):
    answer = 0
    tree = [[numbers[0],0-numbers[0]]]   
    for index,number in enumerate(numbers):
        if index > 0:
            depth = []
            for item in tree[index-1]:                
                depth.append(item+number)
                depth.append(item-number)
            tree.append(depth)
    for item in tree[-1]:
        if item == target:
            answer+=1
    return answer

if __name__ == '__main__':    
    print(solution(arr[0],arr[1][0]))

