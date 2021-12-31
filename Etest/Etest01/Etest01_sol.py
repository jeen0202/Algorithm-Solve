
# 비교를 위해 최소 시간단위로 변경
n,m = 5,4
ans = 0
selected= []
date = ["MO","TU","WE","TH","FR"]

def day_map(time) :
    #변환
    return time

def conflict(A,B): # 시간을 비교
    A = parse(A)
    B = parse(B)
    #max() min() 비교
    for a in A:
        for b in B:
            
def parse(tz) : # 시간을 적절하게 변환 180분 -> 90분*2개    
    return tz

#dfs를 사용
def dfs(idx,schedule):
    if idx== len(schedule):
        return 1
    ret = 0
    for j in schedule[idx]: #j 시간에 들을것
        false = True
        for k in schedule[idx+1]:
            if conflict(j,k) : #겹치면 실패
                flag = False