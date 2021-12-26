import sys
sys.stdin = open("Baekjoon/DP/RGBDistance/input.txt","r")

def solution():
    N = int(input())
    data,answer = [],[]    
    for _ in range(N):
        data.append(list(map(int,input().split())))
        temp = data[-1]
        if not len(answer):
            answer.append((temp.index(min(temp)),min(temp)))
        elif len(answer)==1:
            temp[answer[-1][0]]= 1001
            answer.append((temp.index(min(temp)),min(temp)))
        else:
            temp[answer[-1][0]] = 1001
            #temp[answer[-2][0]] = 1001
            answer.pop()
            mini = 2000
            result = [-1,-1]
            for i in range(3):
                for j in range(3):
                    if data[-1][i]+data[-2][j]< mini:
                        mini = data[-1][i]+data[-2][j]
                        print(mini)
                        result = [i,j]
            answer.append((result[0],temp[result[0]]))
            answer.append((result[1],temp[result[1]]))
    #print(data)
    print(answer)
    print(sum(item[1] for item in answer))
if __name__ == "__main__":
    solution()