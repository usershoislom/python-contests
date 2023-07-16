from __future__ import print_function
from functools import wraps
import sys 

def takes(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            for arg, arg_type in zip(args, types):
                if not isinstance(arg, arg_type):
                    raise TypeError #(f"Expected {arg_type}, but got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
exec(sys.stdin.read()) 
