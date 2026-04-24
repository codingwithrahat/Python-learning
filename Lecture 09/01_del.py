class stu:

    def __init__(self, name):
        self.name = name
    
s1 = stu("Rahat")
print(s1.name)   #print Rahat

del s1.name

print(s1.name)  #not define

del s1

print(s1.name)  #is not define, cz whole obj deleted