# 돌무더기
# 완전탐색
# 연산 법칙 = 총개수 - n + 2  #unique
# 사전 역순을 위해 맨끝 부터
def solution(stones,k):
    if n>2 and (sum-k) % (n-2) != 0 :
        return -1
    if sum <k :
        return -1

