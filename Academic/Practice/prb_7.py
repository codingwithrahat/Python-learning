


import PySimpleGUI as sg

age = int(input('Enter you age : '))

if age < 18:
    sg.popup_error('Age must be greatehr or equal to 18')