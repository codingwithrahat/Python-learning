#using while

n = 5

f = 1

i = 1

while i <= n:
    f *= i
    i+=1

print(f)

#using for
n = 5
f = 1
for i in range(1, n + 1):
    f *= i

print(f)

