"""
for loop
"""

l = [1, 2, 3, 1, 2]


for i in l:
    print(i)


for i in range(3, 6):   #start 3 and end at 5
    print(i)            #3 4 5


#sum 
s = 0
for i in l:
    s += i
print(s)


"""
while loop
"""

i = 0
while i < 15:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 10:
        break