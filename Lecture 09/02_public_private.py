class acct:

    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass          # __ this  make the variable private

    def reset_pass(self, acc_pass):
        self.__acc_pass = acc_pass            # private var - can only be accessed within the class
                     
    def __hello(self):                      #private method
        print("Hello")

    def wel(self):
        self.__hello()
    

a1 = acct(1, 45)

print(a1.acc_no)
# print(a1.acc_pass) #error

a1.reset_pass(46)

#a1.hello() #error

a1.wel()
    
