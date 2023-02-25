from functools import reduce

list_a = [2, 3, 5, 4, 6, 7, 8]
map_a = map(lambda x:x%2, list_a)
print(list(map_a))

print("------------@---------------")
tuple_b = (1, 2, 4, 7, 3, 5, 4)

map_list = map(lambda i, j: i + j, list_a, tuple_b)
print(map_list)
print(list(map_list))

print("-------------@--------------")

#check for filter
filter_c = filter(lambda i:i%2==0, list_a)
print(list(filter_c))

print("-------------@--------------")

#Filter function uses conditional statment to iterate over the list
filter_d = filter(lambda i:True if i>=5 else False , list_a)
print(list(filter_d))

print("-----------@---------------")

        #reduce fumction perform operation on elements in a list
#The below reduce function add all the elements in a list
reduce_d = reduce(lambda i,j:i+j, tuple_b)
print(reduce_d)
print("-----------@----------------")

reduce_e = reduce(lambda i,j:i-j, tuple_b)
print(reduce_e)
