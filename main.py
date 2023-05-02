def my_decorator(func):
    def wrapper():
        return func()+10
    return wrapper
@my_decorator
def example_function():
    n=int(input())
    return n
print(example_function())