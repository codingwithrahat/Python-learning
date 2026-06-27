class car:

    color = "black"

    @staticmethod
    def start():
        print("Car Started")
    
    @staticmethod
    def stop():
        print("Car Stopped")

class BMWcar(car):
    def __init__(self, name):
        self.name = name
    

c1 = BMWcar("bm1")

print(c1.name)

c1.start()
c1.stop()

print(c1.color)



