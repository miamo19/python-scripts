name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt it has come to an end and you can go left or right. which way would you like to go? ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? type 'walk' to walk around it or 'swim' to swim accross: ").lower()

    if answer == "swim":
        print("You swim accross and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of the water and you lost the game")
    else:
        print("Not a valid option. you lose! ")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?").lower()
    if answer == "cross":
        answer= input("You cross the bridge and  meet a stranger. Do you talk to them? (Yes/No)? ").lower()

        if answer == "yes":
            print("You talk to the stranger and they gave you gold and you Win")
        elif answer == "no":
            print("You ignore the stranger and they feel offented and you lose.")
        else:
            print("Not a valid option, You lose! ")
    elif answer == "back":
        print("you go 'back', you will lose")
        if answer == "back":
            print("You Lose!!")

else:
    print("Not a valid optionm, You lose! ")