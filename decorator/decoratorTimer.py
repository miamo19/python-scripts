import datetime

def log(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as f:
            f.write("call function with "+ " " .join([str(arg)for arg in args]) + " at " + str(datetime.datetime.now())+ "\n")
        val = func(* args, ** kwargs)
        return val
    return wrapper

@log
def run(num1, num2, num3):
    print(num1 + num2 + num3)

run(1, 3, c=9)
