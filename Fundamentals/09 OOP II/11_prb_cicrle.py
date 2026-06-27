from math import pi

class circle:

    def __init__(self, r):
        self.r = r

    def area(self):
        print(pi * self.r ** 2)
    
    def per(self):
        print(2 * pi * self.r)

c1 = circle(21)

c1.area()
c1.per()
    