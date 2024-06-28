from functools import lru_cache

@lru_cache
def loop_py(n: int) -> int:
    j = 0
    for i in range(n):
        j += 1
    return j