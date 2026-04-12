def f():
    print("hi")

f()


def f(name):
    print(f"hi {name}")

f("rahat")


def pc():
    color = "red"  #internal var or local var
    print(color)

color = "blue"  #global var
print(color) #blue

pc() #red




def pn(high, low):
    print(high, low)

pn(3, 10)
pn(low=3, high=10)



def mn(a, b):
    return a * b

m = mn(3, 4)

print(m)




def p_list(l):
    for i in l:
        print(i)

l = [1, 2, 4, 1]
p_list(l)




def add_tax(taka):
    return 0.03 * taka

def buy_item(taka):
    return taka + add_tax(taka)

final_cost = buy_item(50)
print(final_cost)


