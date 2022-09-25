   #program adding three complex number,
class Complex:
    def __init__(self, real, img):             #argument real and imaginary part of the complex number is declared
        self.real = real
        self.img = img

    def add(sel, num, num2):
        real1 = sel.real + num.real + num2.real
        imag1 = sel.img + num.img + num2.img
        result = Complex(real1, imag1)
        return result


            #Instance Object
n1 = Complex(2, 5)
n2 = Complex(3,7)
n3 = Complex(-4,-3)
result = n1.add(n2,n3)
print("The imaginary part of complex n1 is: ",result.img)