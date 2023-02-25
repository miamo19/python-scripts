from functools import reduce

list_a = [2, 3, 5, 4, 6, 7, 8]
map_a = map(lambda x:list_a%2, list_a)
print(list(map_a))

print("------------@---------------")
y = [1, 2, 4, 7, 3, 5, 4]

map_list = map(lambda i, j: x + y, x,y)
print(map_list)
print(list(map_list))

print("-------------@--------------")

#check for filter
c = filter(lambda i:i%2==0, x)
print(list(c))

print("-------------@--------------")

#Filter function uses conditional statment to iterate over the list
d = filter(lambda i:True if i>=5 else False , x)
print(list(d))

print("-----------@---------------")

        #reduce fumction perform operation on elements in a list
#The below reduce function add all the elements in a list
z = reduce(lambda i,j:i+j, y)
print(z)
print("-----------@----------------")

m = reduce(lambda i,j:i-j, y)
print(m)
