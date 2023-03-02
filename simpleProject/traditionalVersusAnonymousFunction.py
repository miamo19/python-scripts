import math
from functools import reduce

#calculating area of a circle with traditional function
def area(radius):
    return math.pi * (radius**2)

radii = [2, 5, 7.1, .3, 10]
areas = []
for i in radii:
    a = area(i)
    x =areas.append(a)

print(areas)
print("--------------------------")

#finding the area of the circle using map function take just one line of code
area1 = list(map(lambda radii:radii**2*pi, radii))
print(area1)


print("--------------------------")
#using map function dividing all the areas of the circle by 2
mapList = list(map(lambda area :area/2, areas))
print(mapList)
print("--------------------------")

#using reduce function add all the areas in the list
addArea = reduce(lambda value_1,value_2: value_1+value_2, areas)
print(addArea)

print("--------------------------")

#lambda Function that multiplies two variables
lam = (lambda numb_1,numb_2: numb_1*numb_2)
print(lam(5,5))
