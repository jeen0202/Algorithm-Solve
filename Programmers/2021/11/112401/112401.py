import sys
sys.stdin = open(sys.argv[1],'r')
arr  = [list(map(list,input().split())) for _ in range(3)]


def solution(N,road,K):
    answer = 1
    dict = {}
    for index in range(1,N+1):
        temp = []
        for w in road:
            route =w[:-1]
            time = w[-1]
            if index+1 in route:
               temp[index].append(route,time)
        dict[index] = temp  
    
    print(dict)
    
    return answer

if __name__ == '__main__':    
    print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))

