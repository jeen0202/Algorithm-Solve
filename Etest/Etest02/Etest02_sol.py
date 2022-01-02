# 돌무더기
# 완전탐색
# 연산 법칙 = 총개수 - n + 2  #unique
# 사전 역순을 위해 맨끝 부터
import sys

mem= []
def conv(stones):
    res = 0
    for x in stones:
        res = res*25+x
    return res

def dfs(stones,k,path):    
    mem.append(conv(stones))    
    cnt_k,cnt_0 = 0,0
    # 조건확인
    for x in stones:
        if x==k :
            cnt_k +=1
        if x==0 :
            cnt_0 +=1
    # 조건 충족시 경로 반환
    if cnt_0 == len(stones)-1 and cnt_k == 1:
        return path
    # 역순으로 완전탐색
    for i in range(len(stones)-1,-1,-1):
        flag = True
        stones[i] +=2
        for j in range(len(stones)):
            stones[j] -=1
            if stones[j] < 0:
                flag = False
        #print(stones)
        if flag and conv(stones) not in mem:
            res = dfs(stones,k,path+str(i+0))
            print(path)
            if res != -1:                
                return res
        stones[i] -= 2
        for j in range(len(stones)):
            stones[j] +=1
            
def solution(stones,k):
    sum = 0
    n = len(stones)
    for x in stones:
        sum +=x
    if n>2 and (sum-k) % (n-2) != 0 :
        return "-1"
    if sum <k :
        return "-1"
    return dfs(stones,k,"")

if __name__ == "__main__":
    #sys.setrecursionlimit(50000)
    print(solution([1, 3, 2],3))
    #print(f"mem : {mem}")

