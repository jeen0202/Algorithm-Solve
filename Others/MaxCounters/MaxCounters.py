def solution(N, A):
    mcnt,mnum = 0,0
    cnt= [0]*N
    for item in A:
        if item==N+1:
            mcnt = mnum
            continue
        cnt[item-1] = max(cnt[item-1]+1,mcnt+1)
        mnum = max(mnum,cnt[item-1])
    cnt = [max(mcnt,cnt[j]) for j in range(N)]
    return cnt

if __name__ == "__main__":
    solution(5,[3,4,4,6,1,4,4])
