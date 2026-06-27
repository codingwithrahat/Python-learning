'''
1.Write a Python program that takes five integer
numbers from the user
and show the largest and smallest number.
'''

i = 0

mx = -float('inf')
mn = float('inf')

while i < 5:
    
    x = int(input())

    if x > mx:
        mx = x
    
    if x < mn:
        mn = x

    i = i + 1


print(mx, mn)