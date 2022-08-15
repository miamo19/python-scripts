#program check if the  number enter is a primw number or not
def prime():
    #take input from user for the checking
    num = int(input("Enter the Number: "))
    flag = False
    if num>1:
        #check foe factor
        for i in range(2,num):
            if (num%i==0):
                #if factor is found: set flag to be True
                flag =True
                #break out of the loop
                break
    else:
        flag=True
    #check if flag is True or not
    if flag==True:
        print("Number is not Prime")
    else:
        print("Number is a prime Number")

prime()