#Decorator function contruction
def smart_div(func):
    def inner(numb1, numb2):
        if numb1<numb2:
            numb1,numb2 = numb2,numb1
        return func(numb1, numb2)
    return inner

#Decorator function used
@smart_div
def div(numb1, numb2):
    print(numb1/numb2)
div(2,4)

print("---------------------------")
#second example for decorator
def func1(func):
    def wrapper():
        print("Started!")
        func()
        print("Stopped")
    return wrapper

@func1
def f1():
    print("Hello World")
f1()

print("------------------------")

@f
def f2():
    print("We are the chosen generation")
    
f2()

#with decorators, we can add extract features in an existing function
