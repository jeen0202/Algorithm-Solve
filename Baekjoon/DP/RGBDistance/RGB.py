import sys
sys.stdin = open("Baekjoon/DP/RGBDistance/input.txt","r")

def solution():
    N = int(input())
    data,answer = [],[]    
    for i in range(N):
        data.append(list(map(int,input().split())))
        temp = data[-1]
        if not len(answer):
            answer.append(temp)
        else:
            answer.append(temp)
            answer[i][0] = min(answer[i-1][1], answer[i-1][2])+temp[0]
            answer[i][1] = min(answer[i-1][0], answer[i-1][2])+temp[1]
            answer[i][2] = min(answer[i-1][0], answer[i-1][1])+temp[2]
    print(min(answer[N-1][0],answer[N-1][1],answer[N-1][2]))
if __name__ == "__main__":
    solution()