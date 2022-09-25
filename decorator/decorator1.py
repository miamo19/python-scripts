#decorator function
def smart_div(func):
    def inner(a, b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
@smart_div
def div(a, b):
    print(a/b)
div(2,4)

print("---------------")
#second example for decorator
def f(func):
    def wrapper():
        print("Started!")
        func()
        print("Stopped")
    return wrapper

@f
def f1():
    print("Hello World")
f1()

print("---------------------")

@f
def f2():
    print("We are the chosen generation")
f2()

#with decorators, we can add extract features in an existing function