#open a file in the write mode
file = open("demo2.txt", 'w')
try:
    for i in range(5):
        file.write('\t The situation in the northwest and southwest is %d\n' %i)  #%i or %(i+1)
finally:
    file.close()

file1 = open('demo2.txt', 'r')
print(file1.read())
file1.close()


#The above code for opening a file can be writen as below👇👇👇
"""
with open("demo2.txt", "w") as file:
    try:
    for i in range(5):
        file.write('\tThe situation in the northwest and southwest is %d\n' %i)  #%i or %(i+1)
    finally:
        file.close()
    with open("demo2.txt", "r") as fil:
        print(fil.read())
"""
