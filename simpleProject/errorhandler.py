#open a file in the write mode
file = open("demo2.txt", 'w')
try:
    for i in range(5):
        file.write('\tThe situation in the northwest and southwest is %d\n' %i)  #%i or %(i+1)


finally:
    file.close()

fil = open('demo2.txt', 'r')
print(fil.read())
fil.close()
