# 3차원 DP dp[cnt][sum][odd-sum]
# 사용한 원소의 개수, 사용한 원소의 총합, 사용한 원소중 홀수번째의 합
# dy[N][M][M/2] = 정답..?
import sys
MOD = 100000007

def solution():
    N,M,K = map(int, input().split())
    dy = [[[0 for _ in range(M+1)]for __ in range(M+1)]for ___ in range(N)]
    dy[0][0][0]=1
    for i in range(1,N+1):
        for s in range(1,M+1):
            if s >i *K :
                break
            for os in range(1,M+1):
                if os >s:
                    break
                if i %2 == 1:
                    for l in range(1,K+1):
                        if s<1 or os <l:
                            break
                        dy[i][s][os] += dy[i-l][s-l][os-l]
                        dy[i][s][os] %= MOD
    print(dy[N][M][K]//2)

if __name__ == "__main__":
    solution()
