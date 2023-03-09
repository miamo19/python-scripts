import time
#Function for timing the execution of another function (function use for decorating other function)
def timer(func):
    def wrapper():
        before = time.time()
        try:
            func()
        except Exception as e:
            print("Invalid input: ", e , "\nEnter a positve whole number:")
        print("function took. ", time.time() - before, "second")

    return  wrapper

#Decorate the functipn to check prime number
@timer
def prime():
    #take input from user for the checking
    num = int(input("Enter number: "))

    if num != 1:

        for i in range(2,num):
            if (num%i ==0):
                print("Number is not prime")
                break
        else:
            print("Number is Prime number")

    else:
        print("Number is not prime number")
prime()
