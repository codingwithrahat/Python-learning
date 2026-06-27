'''
8. Write a Python program that will take input
from a user as an age. So, check whether the
number is greater than 50 or not.
user] Sample Input and output:
Input Outpu
20 your are not allowed
50 You are allowed
The field is empty
60 you are allowed
49 You are not allowed
'''

a = int(input())

if a >= 50:
    print('allow')
else :
    print('not allow')