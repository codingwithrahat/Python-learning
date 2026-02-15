#type conversion (bt default change)

a = 2
b = 4.25
c = 3

sum = a + b  #by default convert to float
sum2 = a + c #not convert to float

print(sum)
print(sum2)


#type casting

r = "2"
s = 3
# print(a + s) error

r = int("2")
print(r + 3)

a = str(3.24)
b = float(2)    #2.0

print(type(a))

print(b)
