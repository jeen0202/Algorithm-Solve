# 3Kg, 5Kg의 설탕봉지로 NKg의 설탕을 배송해야될때 최소 개수

def solution(N):
    cache = [0,-1,-1,1,-1,1]
    if N>5:
        for i in range(6,N+1):
            if i>5 and cache[i-5] >0 :
                cache.append(cache[i-5]+1)
            elif cache[i-3] >0 :
                cache.append(cache[i-3]+1)
            else:
                cache.append(-1)               
    return cache[N]

if __name__ == '__main__':    
    print(solution(18))
    print(solution(4))
    print(solution(6))
    print(solution(9))