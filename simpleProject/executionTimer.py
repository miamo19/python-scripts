import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("function took. ", time.time() - before, "Second")

    return  wrapper

@timer
def run():
    time.sleep(1)

run()
