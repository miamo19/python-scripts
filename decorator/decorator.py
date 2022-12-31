#Example of a function to be used as a decorator
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Started")

        arg = func(*args, **kwargs)
        print("Stopped")
        return arg

    return wrapper

@decorator
def f1(a):
    print(a,"Is Better")
    print("+++A decorated function ++++")
f1('hibrahim')

print("------------------------")

@decorator
def f2(x,y):
    print("the sum of: ", x , " and ", y ," = ", x+y)

f2(2, 8)

print("------------------------")

@decorator
def add(x, y):
    return x+y

print(add(4,5))
