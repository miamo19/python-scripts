x = 5.0
y = 0.0

try:
    print("Resource open")
    print(x/y)

except Exception as e:
    print("You can not perform the operation:", e)

finally:
    print("Resource close")
print("Beautiful")