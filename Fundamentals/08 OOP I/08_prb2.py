class bank:

    def __init__(self, balance):
        self.balance = balance
    
    def debit(self, amount):
        self.balance -= amount
        self.get_bal()

    def credit(self, amount):
        self.balance += amount
        self.get_bal()

    def get_bal(self):
        print("Current Balance", self.balance)


b1 = bank(5000)

b1.debit(500)
b1.credit(1000)

b1.get_bal()
