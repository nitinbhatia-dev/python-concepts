import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {end - start:.6f} seconds to complete')
        return result
    return wrapper


@timeit
def yieldTest():
    for i in range(1,3):
        yield i

if __name__ == "__main__":
    t = yieldTest()
    print(next(t))
    print(next(t))
    print(next(t)) # this will throw StopIteration Exception