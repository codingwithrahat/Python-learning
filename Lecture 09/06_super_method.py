class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print('Car Started')

    @staticmethod
    def stop():
        print('Car Stopped')
    

class ToyotaCar(Car):
    def __init__(self, brand, type):
        self.brand = brand
        super().__init__(type)
        super().start()


# t1 = ToyotaCar('prius')
# print(t1.type) #will give error

t2 = ToyotaCar('prius', 'electric')  #print - Car Started
print(t2.type)