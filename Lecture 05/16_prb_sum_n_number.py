#using while

n = int(input("Enter Number : "))

sum = 0

i = 1

while i <= n:
    sum += i
    i+=1

print(sum)

#using for

n = int(input("Enter Number : "))

sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)
