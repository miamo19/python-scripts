#variables                           dataType

integer_x = 15                       #interger type

float_y = 5.3                        #float type
float_z = 3.0

first_name = "Miami"                 #string type
second_name = "yve chalton" 
last_name = "HYACINTH"

#converting a float (float_y)  to interger and storing its value in another variable i
i = int(float_y)
print(i)      

#converting an interger integer_x to a float and storing its value in another variable f
f = float(integer_x)
print(f)     

#multiplication of variable integer_x and float_y and print the result
print("{0} * {1} = {2}".format(integer_x,float_y, integer_x*float_y))

#capitilize the content of the variable second_name
print(second_name.capitalize())

#variable first_name is printed in uppercase letter
print(first_name.upper())

#variable last_name is printed in lowercase letter
print(last_name.lower())

#check if variable first_name is uppercase and answer is in boolean
print(first_name.isupper())

#print a statement with multiple datatype
print("Mr. %s are you %d years old? " %(first_name,x), "\n\t Why ask?")
