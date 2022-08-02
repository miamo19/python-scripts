class Market:
    def __init__(self, *arg, **arg1):
        print(arg)
        for k, v in arg1.items():
            print(k,': ',v)


market1 = Market('yvan',25,'Hyasan',55, books=500, pens=100, pencils=25, Numbers='three')
