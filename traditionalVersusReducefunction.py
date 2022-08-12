from functools import reduce

#traditional function script
def mult(lst1):
    prod = lst1[0]
    for i in range(1,len(lst1)):
        print(i)
        prod *=lst1[i]
    return prod
print (mult([4,3,2,5]))

print("------------------")

#Lambda function performing the same task as the function above
list1 = [4, 3, 2, 5]
print(reduce(lambda a,b: a*b, list1))