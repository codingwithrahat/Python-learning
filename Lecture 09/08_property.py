class Stu:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math

        self.per = str((phy + che + math) / 3) + "%"


s1 = Stu(98, 97, 99)
print(s1.per)

s1.phy = 86
print(s1.phy) #86

print(s1.per)  # still same , like before




# solve way 1

class Stu2:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math
        self.per = str((phy + che + math) / 3) + "%"

    def calPer(self):
        self.per = str((self.phy + self.che + self.math) / 3) + "%"


s2 = Stu2(98, 97, 99)
print(s2.per)

s2.phy = 86
s2.calPer()

print(s2.per) 




#solve way 2 (property decorator)

class Stu3:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math

    # property lets you access method like a variable
    # property method must return a value.
    @property  
    def calPer(self):
        return str((self.phy + self.che + self.math) / 3) + "%" 

s3 = Stu3(98, 97, 99)
print(s3.calPer)

s3.phy = 86

print(s3.calPer) 