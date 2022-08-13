def smart_div(func):
    def inner(a, b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

@smart_div
def div(x, y):
    print(x/y)

div(2,4)

@smart_div
def div1(q, p):
    print(q/p)
smart_div(div1(7,32))