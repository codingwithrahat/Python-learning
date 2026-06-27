'''13. Write a Python program that will take two
interger umber from user. if user put first
number 4 and second number 9 then print the value

4 5 6 7 8 9. Note: first number is always smaller
than second number .if user put first number
large and second number small then it will alert
the message(“Please give first number small and
second number large”).
'''

import PySimpleGUI as sg

a = int(input('Enter first number: '))
b = int(input('Enter 2nd number: '))

if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    sg.popup_error('Please give first number small and second number large')