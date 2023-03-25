# The Parent Class (SuperClass)
class User:
    def __init__(self, name, age, gender):   #special method (contructor)
        self.name = name
        self.age = age
        self.gender = gender

    def show_detail(self):                   #method
        print("Show Personal details: \n")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

#This Class Child inherite from the Parent Class User (SuperClass)
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Your amount deposited is: {self.amount}  you updated balance is: $ {self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        if self.balance >= self.amount:
            self.balance = self.balance - self.amount
            print(f"\nYour withdrawal amount is: $ {self.amount} Your new balance is: $, {self.balance}")
        else:
            print("insufficient fund $", self.balance)

    def viewBalance(self):
        self.show_detail()
        print("Account balance is: ", self.balance)


u = Bank('lucy', 25, 'F')
u.deposit(15000)

u.withdraw(23000)
u.viewBalance()
