import time
from functools import wraps
# 함수를 메모이제이션하는 데코레이터 생성
def memoizer(func):
    cache = {}

    @wraps(func)
    def memoizer(*args,**kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args,**kwargs)
        return cache[key]

    return memoizer

@memoizer
def expensive_fn(a,b):
    time.sleep(1)
    return a + b

before = time.time()
print(expensive_fn(1,2))
print(f'first called : {time.time()-before}')

before = time.time()
print(expensive_fn(1,2))
print(f'Second called : {time.time()-before}')
