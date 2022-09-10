from dataclasses import dataclass

# this example is complex with the __init__() method
'''
class User:
    def __init__(self, first_name: str, last_name:str ):
        self.first_name = first_name
        self.last_name = last_name
'''
#This is the simplify __init__() method with the decorator
@dataclass
class User:
    first_name: str
    last_name : str

patrick = User("Patrick", "Smith")
print(repr(patrick))

print("--====---====----=======-----=====---====")
#Defaut values
@dataclass
class Users:
    #here is the instance variable from the __init__() method
    first_name: str
    last_name : str = "vince"

patrick0 = Users("Patrick")
print(repr(patrick0))

print("--====---====----=======-----=====---====")
#Example with class variables distinc from instance variable
#for this, import from typing ClassVar

from typing import ClassVar
@dataclass
class Use:
    c:ClassVar[int]   #class variable
    first_name: str    #instance variable from __init__()
    last_name : str    #instance variable from __init__()

patrick1 = Use("Patrick", "Smith")
#print(repr(patrick1))
print(patrick1.__dict__)

print("--====---====----=======-----=====---====")
#if you want to give a default value to class variable (ClassVar)
@dataclass
class Utilisateur:
    name: ClassVar[str]= 'vince'
    first_name: str
    last_name : str = "vince"

patrick2 = Utilisateur("Patrick")
print(repr(patrick2))

print("--====---====----=======-----=====---====")
#if there are action you want to execute automatically after the __init__()
@dataclass
class Utilisateurs:
    num:ClassVar[int] = 2
    first_name: str
    last_name: str

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"
patrick3 = Utilisateurs("patrick", "smith")
print(patrick3.full_name)
