from functools import reduce

#traditional function script
def mult(list1):
    prod = list1[0]
    for i in range(1,len(list1)):
        print(i)
        prod *=list1[i]
    return prod
print (mult([4,3,2,5]))

print("------------------")

#Lambda function performing the same task as the function above (Traditional function)
list1 = [4, 3, 2, 5]
print(reduce(lambda value_1,value_2: value_1*value_2, list1))
