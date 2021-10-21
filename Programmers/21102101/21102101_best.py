import sys
sys.stdin = open(sys.argv[1],"r")
arr  = [list(map(int,input().split())) for _ in range(2)]

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

if __name__ == "__main__":
    print(solution(arr[0],arr[1]))