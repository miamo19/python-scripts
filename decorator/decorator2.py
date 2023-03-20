def smart_div(func):
    def inner(value1, value2):
        if value < value2:
            value1, value2= value2, value1
        return func(value1, value2)
    return inner

@smart_div
def div(num1, num2):
    print(num1/num2)
    print(num1*num2)

div(14,3)

@smart_div
def div1(n1, v2):
    print(v1/v2)
smart_div(div1(7,32))
