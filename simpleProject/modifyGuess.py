# computer will guess from a random values provider the user know the correct number
import random

def computer_guess(x):
    high = x
    low = 1
    feedback = " "
    n = 1
    while feedback != "c":
        if high != low:
            guess = random.randint(low, high)
            print(guess)
        else:
            guess = low

        user_num = 3

        if guess !=user_num:
            feedback = input(f"Is {guess} too low , too high? ")
            try:
                if feedback == 'h'or feedback=='H':
                    print("too high")
                    high = guess-1
                elif feedback == 'l' or feedback=='L':
                    print("too low")
                    low = guess+1
            except TypeError as e:
                print("Check the that your response is either 'h' or 'l' and try again", e)
            if n==3:
                print("You Fail!! You exhauted your trial.")
                exit()
            n+=1
        else:
            print("you Won!! Correct Number")
            exit()

    print("you Won!! Correct Number")

computer_guess(10)
