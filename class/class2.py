#Arg and Kwarg one takes a list and the other takes a dictionary
class Market:
    def __init__(self, *arg, **arg1):
        print(arg)
        print(arg1)
        for k, v in arg1.items():
            print(k, ': ', v)

market1 = Market('yvan',25,'Hyasan',55, books=500, pens=100, pencils=25, Numbers='three')
