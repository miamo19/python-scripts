class Hello:
    def __init__(self, name, marks): 
        self.__name = name
        self.__marks = marks
        
    def set_name(self, value):
        self.__name = value
        
    def get_name(self):
        return self.__name

#Create an object of the class Hello
hello = Hello('niano', 'fff')
print(hello.get_name)
