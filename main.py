#1
def my_decorator(func):
    def wrapper():
        return func()+10
    return wrapper
@my_decorator
def example_function():
    n=int(input())
    return n
print(example_function())
#2
import time
def decorator(func):
    def wrapper(*args, **kwargs):
        stat_time=time.time()
        result = func(*args, **kwargs)
        end_time =time.time()
        print(end_time - stat_time)
        return result
    return wrapper
@decorator
def example_function(x):
    time.sleep(1)
    return x
print(example_function(777))
#3