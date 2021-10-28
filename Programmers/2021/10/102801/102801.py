import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(str,input().split())) for _ in range(2)]
arr[1] = list(map(int,arr[1]))

def solution(orders,course):
    print(orders)
    print("==============")
    answer = []
    for max in course:
        for i in orders:
            for j in orders:
                if len(i.serach(j)) == max :
                    print(orders[i].match(orders[j]))
                    
    return answer   

if __name__ == '__main__':    
    print(solution(arr[0],arr[1]))

