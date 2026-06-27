class stu:

    def __init__(self, name):
        self.name = name

    @staticmethod      #decoroder - convert a function to a methods, no need self
    def wel():
        print("Hello")

     
        


s1 = stu("Rahat")

s1.wel()
