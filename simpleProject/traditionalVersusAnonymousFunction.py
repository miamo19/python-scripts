import math
from functools import reduce

#calculating area of a circle with traditional function
def area(r):
    return math.pi * (r**2)

radii = [2, 5, 7.1, .3, 10]
areas = []
for i in radii:
    a = area(i)
    x =areas.append(a)

print(areas)
print("--------------------------")

#finding the area of the circle using map function take just one line of code
area1 = list(map(area, radii))
print(area1)


print("--------------------------")
#using map function dividing all the areas of the circle by 2
mapList = list(map(lambda x :x/2, areas))
print(mapList)
print("--------------------------")

#using reduce function add all the areas in the list
addArea = reduce(lambda x,y:x+y, areas)
print(addArea)

print("--------------------------")

#lambda Function ta
lam = (lambda x,y:x)
print(lam(5,5))
