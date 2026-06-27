'''
2. Suppose you need to write a program to take a
survey of university
students' extra curriculum activities. Now you
can use IF ELSE statement to do
this:
->If a user inputs “brilliant” then show “The
Student is more active and sincere”.
->If a user inputs “better” then show “The
Student is trying to join extra curriculum
activities”.
->If a user inputs “good” then shows “The Student
is learn about extra curriculum
activities”.
->If a user inputs “Nothing” then show “The
Student does not join any extra
curriculum activities Yet”. 
'''

str = input()

if str == "brilliant":
    print('The Student is more active and sincere\n')
elif str == 'better':
    print('The Student is ltrying to join extra curriculum activities\n')
elif str in 'better':
    print('The Student is learn about extra curriculum activities\n')
else:
    print('The Student does not join any extra curriculum activities Yet')
    
