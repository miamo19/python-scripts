# This  function to guess number out of a range for a limited trial of 3
#For this, we have to import the module "random" first
import random

def guess(x):
    ranNum = random.randint(1,x)
    guess, n= 0, 0

    while guess != ranNum or n<=2:
        try:
            guess = int(input(f"Enter guess number fron 1 to {x}: "))

            if guess >ranNum:
                print("The value is too high")
            elif guess<ranNum:
                print("The number is to low")
            else:
                print("You won")
                exit()

        except Exception as e:
            print('value to be enter must be an interger: ',e)

        if n!=2:
            n+=1
        else:
            print("Number of trial exhauted. You fail!!!")
            exit()
    print("You won")
guess(10)
