class car:

    @staticmethod
    def start():
        print("Car Started")
    
    @staticmethod
    def stop():
        print("Car Stopped")

class Toyotacar(car):
    def __init__(self, name):
        self.name = name

class fortuner(Toyotacar):
    def __init__(self, type):
        self.type = type
    
c1 = fortuner("diesel")

c1.start()