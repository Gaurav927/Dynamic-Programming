def power(base, rise):
    result = 1
    for num in bin(rise)[2:][::-1]:
        if int(num):
            result *= base
        base = base*base
    return result

from functools import lru_cache

@lru_cache(maxsize=None)
def recurse_power(base, rise):
    # print('rise---->',rise)
    if rise<=1:
        return base if rise ==1 else 1
    
    if rise%2:
        return base * recurse_power(base, (rise-1)//2)*recurse_power(base, (rise-1)//2)
    
    return recurse_power(base, rise//2)*recurse_power(base, rise//2)

from timeit import timeit

print('iterative -->',timeit('power(10, 2000)',globals=globals(), number=100000))

print('recusrsive -->',timeit('recurse_power(10, 2000)',globals=globals(), number=100000))

# print(recurse_power(10, 100))