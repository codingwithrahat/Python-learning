# 9.Write a Python program to find an odd number between 1 to 200.


for i in range(1, 201):     #last odd number will be 199
    if i % 2 != 0:
        print(i)