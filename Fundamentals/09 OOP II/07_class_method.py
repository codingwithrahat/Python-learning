class Person:
    name = 'annonymous'

    def changename(self, name):
        self.name = name

p1 = Person()
p1.changename('Rahat Hossan')

print(p1.name) #Rahat Hossan
print(Person.name)  #annonymous , cz - normal method cng the attributes for objects not for class



#cng class atributes way 1
class Person2:
    name = 'annonymous'

    def changename(self, name):
        Person2.name = name

p2 = Person2()
p2.changename('Rahat Hossan')

print(p2.name) #Rahat Hossan
print(Person2.name)  #Rahat Hossan





#cng class atributes way 2
class Person3:
    name = 'annonymous'

    def changename(self, name):
        self.__class__.name = name

p3 = Person3()
p3.changename('Rahat Hossan')

print(p3.name) #Rahat Hossan
print(Person3.name)  #Rahat Hossan




#cng class atributes way 4 (Class Method)
class Person4:
    name = 'annonymous'

    @classmethod
    def changename(cls, name):
        cls.name = name

p4 = Person4()
p4.changename('Rahat Hossan')

print(p4.name) #Rahat Hossan
print(Person4.name)  #Rahat Hossan

 