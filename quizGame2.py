def question():
    print("Welcome to this Computer Quiz Game. Enjoy answering question!!")
    candidate = input("Would you want to answer our QUIZ?? ").lower()
    if candidate != "yes":
        print("bye bye!!")
        exit()
    print("Be ready ...👇👇👇")
    score = 0

    answer = input("What does the CPU stands for?  ").lower()
    if answer == "central processing unit":
        print("Correct")
        score +=1
    else:
        print("Incorrect")

    answer = input("What does RAM stands for?  ").lower()
    if answer == "read access memory":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    answer = input("What does ROM stands for?  ").lower()
    if answer == "read only memory":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    answer = input("What does GUI stands for?  ").lower()
    if answer == "graphic user interface":
        print("Correct")
        score += 1
    else:
        print("Incorrect")


    answer = input("What does GPU stands for?  ").lower()
    if answer == "graphic processing unit":
        print("Correct")
        score += 1

    else:
        print("Incorrect")

    print("your have "+ str(score) + " question correct.")
    print("your have "+ str((score/5)*100) + "%.")