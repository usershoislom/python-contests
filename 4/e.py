import time
from functools import wraps

def profiler(func):
    count = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        if count == 0:
            wrapper.calls = 0
        count += 1
        wrapper.calls += 1
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        wrapper.last_time_taken = end_time - start_time
        count -= 1
        return result

    wrapper.last_time_taken = 0
    return wrapper

