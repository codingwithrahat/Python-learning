#8.Write a Python program which find out the

a = int(input('Enter number : '))

if a >= 80 and a <= 100:
    print('A+')
elif 30 <= a <= 79:
    print('Pass')
elif a >= 0:
    print('Fail')
else:
    print('INVALID MARK')