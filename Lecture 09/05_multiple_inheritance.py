class a:

    @staticmethod
    def p1():
      print("A")

class b:

    @staticmethod
    def p2():
        print("B")

class c(a, b):

    @staticmethod
    def p3():
        print("C")

c1 = c()

c1.p1()
c1.p2()
c1.p3()