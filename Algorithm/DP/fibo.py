# 메모이제이션을 활용한 팩토리얼
factorial_memo = {}

def factorial(n):
    if n<2:
        return 1
    if n not in factorial_memo:
        factorial_memo[n] = n * factorial(n-1)
    return factorial_memo[n]

if __name__ =='__main__':
    print(factorial(5))