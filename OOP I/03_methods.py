
class stu:

    def __init__(self, name):
        self.name = name
    
    def wel(self):
        print("Hello", self.name)

    def ask(self):              #use self, otherwise 
        print("Any Question?")  #it is treated as a function not class method
        


s1 = stu("Rahat")

s1.wel()
s1.ask()