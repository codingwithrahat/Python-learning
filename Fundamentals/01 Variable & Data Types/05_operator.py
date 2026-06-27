#arithmetic op

b = 5
c = 3

print(b + c)
print(b - c)
print(b * c)
print(b / c)   #1.6666666666666667, float style output
print(b // c)  #1, floor value, int style output
print(b % c)   #2, reminder
print(b ** c)  #125, power


#relational op 
#always return boolean 
a = 2
d = 3

print(a == d) #False
print(a != d) #True
print(a > d)
print(d > a)
print(a >= d)
print(a <= d)


#assignment op
#use for asign values
g = a  #assign a into g
print(g)
g += a # g = g + a
print(g)
g -= a # g = g - a
print(g)
g *= a # g = g * a
print(g)
g //= a # g = g // a
print(g)
g /= a # g = g / a
print(g)
g %= a # g = g % a 
print(g)
g **= a # g = g ** a
print(g)



#logical op
# return True or false
print(not False) # True
print(not True) # False

val1 = True
val2 = False

print(val1 and val2) #False
print(val1 or val2)  #True
