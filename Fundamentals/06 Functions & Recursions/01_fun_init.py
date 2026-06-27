def sum(a, b):              #parameters a, b
    print("Sum")
    return a + b

print(sum(2, 3)) #print sum and also print 5, here a and b are arguments


sum(4, 5) #only print sum


def print_hello():
    print("Hello")

output = print_hello()  #print Hello, 

#now
print(output) #it print None , cz output varibale store nothing, print_hello dosn't return anything


