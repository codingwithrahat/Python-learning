'''
4. Write a Python program that contains an Array
and show the value in
descending order. [In the Array keep any ten
values ]
'''

a = [1, 2, 3, 4, 5, 62, 7, 8, 9, 10]

for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp 

print(a)


