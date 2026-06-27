# Write a Python program that asks the user to input the names of three fruits.
# Store the fruits in a list and display the entire list. Then, display each fruit
# individually by accessing them from the list.Write a Python program that asks the user to input the names of three fruits.
# Store the fruits in a list and display the entire list. Then, display each fruit
# individually by accessing them from the list.

a = []

for i in range(0, 3):
    x = input()

    a.append(x)

print(a)

print(a[0])
print(a[1])
print(a[2])


