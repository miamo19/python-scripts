from functools import reduce

x = [2, 3, 5, 4, 6, 7]
a = map(lambda x:x%2, x)
print(list(a))

print("------------@---------------")
y = [1, 2, 4, 7, 3, 5]

b = map(lambda i, j: x + y, x,y)
print(b)
print(list(b))
print("-------------@--------------")

#check for filter
c = filter(lambda i:i%2==0, x)
print(list(c))
print("---------------------------")

#Filter function uses conditional statment to iterate over the list
d = filter(lambda i:True if i>=5 else False , x)
print(list(d))

print("-----------#----------------")
        #reduce fumction perform operation on elements in a list
#The below reduce function add all the elements in a list
z = reduce(lambda i,j:i+j, y)
print(z)
print("-----------#----------------")
m = reduce(lambda i,j:i-j, y)
print(m)