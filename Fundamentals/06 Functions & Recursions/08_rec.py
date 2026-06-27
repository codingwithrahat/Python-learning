#recursion function

#print  5 to 1
def p(n):
    if(n == 0):
        return
    
    print(n)
    p(n - 1)

p(5)


#retuen n!

def f(n):
    if(n == 0 or n == 1):
        return 1
    return n * f(n - 1)

fact = f(5)

print(fact)