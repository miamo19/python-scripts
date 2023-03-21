#Break keyword goes with while loop
i=0
while i<10:
    if i==5:
        break
    print(i)
    i+=1
    
print("-------------@-----------------")

#Continue keyword also goes with while loop
n=0
while n<10:
    a =n
    n+=1
    if a==5 or a==6:
        continue
    print(a)
print("--------@-------------")

#break keyword also goes with for loop
for v in range(8):
    if v==5:
        break
    print(v)
print("--------------@-----------")

#continue keyword also goes with for loop
for x in range(8):
    if x ==3 or x==6:
        continue
    print(x)
print("END")



