class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, obj2):
        if self.price > obj2.price:
            return True
        else:
            return False
        
o1 = order("chips", 20)
o2 = order("tea", 10)

print(o1 < o2)