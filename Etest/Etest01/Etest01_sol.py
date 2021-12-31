
# 비교를 위해 최소 시간단위로 변경
n,m = 5,4
ans = 0
selected= []
date = ["MO","TU","WE","TH","FR"]

def convTime(time) :
    #변환 : 모든 시간이 동일하게
    day = date.index(time[:2])*60*24
    hour = int(time[3:5])*60
    minute = int(time[6:8])
    return day+hour+minute

def parse(tz) : # 시간을 적절하게 변환 180분 -> 90분*2개    
    # 3시간짜리 수업의 경우 90분씩 쪼개어 파싱
    if len(tz) == 8:
        v = convTime(tz)
        return [(v,v+90),(v+90,v+180)]
    # 90분짜리 2개의 경우 2등분
    else:
        v1 = convTime(tz[:8])
        v2 = convTime(tz[9:])
        return [(v1,v1+90),(v2,v2+90)]
    
def conflict(A,B): # 시간을 비교
    A = parse(A)
    B = parse(B)
    #max() min() 비교
    for a in A:
        for b in B:
            if max(a[0],b[0]) < min(a[1],b[1]):
                return True
    return False

#dfs를 사용
def dfs(idx,schedule):
    if idx== len(schedule):
        return 1
    ret = 0
    for j in schedule[idx]: #j 시간에 들을것
        flag = True
        for k in selected:
            if conflict(j,k) : #겹치면 실패
                flag = False
        if flag:
            selected.append(j)
            ret += dfs(idx+1,schedule)
            selected.pop()
    return ret

def solution(schedule):
    return dfs(0,schedule)

if __name__ == "__main__":
    print(solution([["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"], ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]))