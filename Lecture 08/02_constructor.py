class stu:
    name = "rahat"

    # This function is called automatically whenever a new object is created
    #it called contsuctor
    def __init__(self):   #must init with self, it can be anything like abcd
        print("New Stu")


s1 = stu()  


#default contructor
class bike:

    def __init__(self):
        pass

    #if we not define this function, python will create it automatically 



#parameterized constructor
class car:

    county = "BD"   #class attribute

    name = "Suzuki"

    def __init__(abcd, model, color):   #standard way use self, model or name both work
        abcd.name =  model   #obj attribute
        abcd.color = color
        print("New Car")

c1 = car("bmw", "sky")
print(c1.name, c1.color)

c2 = car("Oddi", "green")
print(c2.name, c2.color)


#both are same for class attributes             
print(c1.county)
print(car.county)


print(c1.name)  #print bmw cz obj attribute priority > class attribute
print(car.name)  #print Suzuki, classs can only access the class attribute
