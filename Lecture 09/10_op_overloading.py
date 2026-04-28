class complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real, "i  +", self.img, "j")

    def add(self, obj2):
        newReal = self.real + obj2.real
        newImg = self.img + obj2.img

        return complex(newReal, newImg)



c1 = complex(2, 3)
c2 = complex(4, 5)

c1.show()
c2.show()

c3 = c1.add(c2)
c3.show()


#anotehr way using dunder
#c3 = c1 + c3  add op in class

class complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real, "i  +", self.img, "j")

    def __add__(self, obj2):
        newRead = self.real + obj2.real
        newImg = self.img + obj2.img

        return complex(newRead, newImg)


c4 = complex(2, 3)
c5 = complex(4, 5)

c4.show()
c5.show()

c6 = c4 + c5
c6.show()