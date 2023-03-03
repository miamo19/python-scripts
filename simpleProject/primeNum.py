#program to check if the  number enter is a prime number or not
def prime():
    num = int(input("Enter the Number: "))  #Take input value from user to check if value is prime number
    flag = False
   
    if num>1:
        for i in range(2,num):    #check for factor
            if (num%i==0):
                            #If the Factor is Found: set flag to be True and break out of the loop 
                flag =True
                break
    else:
        flag=True
  
    if flag==True:
        print("value is not a Prime Number")
    else:
        print("value is a prime Number")

prime()
