import sys
sys.stdin = open("Baekjoon/DP/RGBDistance/input.txt","r")

def solution():
    N = int(input())
    answer = []    
    for _ in range(N):
        data = list(map(int,input().split()))
        if not len(answer):
            answer.append((data.index(min(data)),min(data)))
        else:
        # elif len(answer)==1:
            data[answer[-1][0]] = 1001
            answer.append((data.index(min(data)),min(data)))
        #print(data)
    print(sum(item[1] for item in answer))

if __name__ == "__main__":
    solution()