Dynamic Programming
=====
# 개요
Dynamic Programming은 연산시 메모리의 공간을 더 사용하여 한번 계산한 문제를 다시 계산하지 않도록 구현하여 프로그램의 연산 속도를 비약적으로 증가시키는 방법입니다.

# 조건
* 큰 문제를 작은 문제로 분할 할 수 있는 `부분 반복 문제`
* 작은 문제에서 도출한 최적의 답이 그것을 포함하는 큰 문제에서도 동일 한 `최적 부분 구조`

상기 2개의 조건을 만족할 경우 DP(Dynamic Programming)을 사용 할 수 있습니다.

# 구현 기술 - Memoization(메모이제이션)

프로그램이 동일한 계산을 반복할 떄, 이전에 계산한 값을 메모리(Cache)에 저장함으로써 동일한 계산의 반복 수행을 제거하여, 실행 속도를 빠르게하는 기법

## 접근 방법 01 : Top-Down
- 큰 문제에서 부분 문제로 쪼개가면서, `재귀 호출`을 사용하여 문제를 해결하는 방식

예시
```python
#Top-Down 방식의 피보나치 수열 구현
cache = [0] * 101 #저장을 위한 Cache는 최대 범위보다 1 크게

cache[1] = 1;
cache[2] = 1;

def fib(n):
    if cache[n] != 0:
        return cache[n]
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]
```

## 접근 방법 02 : Bottom-Up
- 아래에서 위로 접근하는 방식으로 부분 문제에서 점차 큰 문제를 해결하는 방식으로 `반복문(for)`를 이용하여 푸는 방법

예시
```python
cache = [0] * 101
d[1] = 1
d[2] = 1
N = 100
for i in range(3,N+1):
    d[i] = d[i-1] + d[i-2]
# 결과 = d[N]
```