#program to check if the  number enter is a prime number or not
def prime():
    #take input from user for the checking if number is prime
    num = int(input("Enter the Number: "))
    flag = False
    if num>1:
        #check for factor
        for i in range(2,num):
            if (num%i==0):
                #if factor is found: set flag to be True and break out of the loop 
                flag =True
                break
    else:
        flag=True
  
    if flag==True:
        print("Number is not Prime")
    else:
        print("Number is a prime Number")

prime()
