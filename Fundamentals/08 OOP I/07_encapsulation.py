class car:

    def __init__(self):
        self.clutch = False
        self.brk = False

    def start(self):
        self.clutch = True
        print("Started")

    def stop(self):
        self.brk = True
        print("Break")
        
        

c1 = car()
c1.stop()


# Encapsulation is a core Object-Oriented Programming (OOP) concept
# that bundles data (attributes) and methods (functions) into a single unit,
# typically a class, while restricting direct access to some components
