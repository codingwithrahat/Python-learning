class car:

    def __init__(self):
        self.clutch = False
        self.brk = False

    def start(self):
        self.clutch = True
        
        print("Started")

c1 = car()
c1.start()

# The user only interacts with the start() method
# Internal details like clutch and brake are hidden
# The user does not need to know how the car actually works
