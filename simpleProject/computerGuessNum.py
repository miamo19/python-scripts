#computer will guess from a random values provider the user know the correct number
#For this we have to import a module "random" first
import random

def computer_guess(x):
    high =x
    low = 1
    feedback = ""

    while feedback != "c":
        if high!=low:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (h), or too low (l) or correct (c)?")
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print("you Won! correct guess")
computer_guess(10)
