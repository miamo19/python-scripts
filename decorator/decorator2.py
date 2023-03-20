def smart_div(func):
    def inner(a, b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

@smart_div
def div(num1, num2):
    print(num1/num2)
    print(num1*num2)

div(14,3)

@smart_div
def div1(q, p):
    print(q/p)
smart_div(div1(7,32))
