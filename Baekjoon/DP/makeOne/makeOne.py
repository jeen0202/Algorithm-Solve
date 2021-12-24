# N = int(input)
def solution(N) :
    cache = [0,0,1,1]
    if N>3:
        for i in range(4,N+1):
            cache.append(cache[i-1]+1)
            if i%3 == 0:
                cache[i] = (min(cache[i//3]+1,cache[i]))
            if i%2 == 0:
                cache[i] = (min(cache[i//2]+1,cache[i]))
    return cache[N]

if __name__ == "__main__":
    print(solution(2))
    print(solution(10))
    
