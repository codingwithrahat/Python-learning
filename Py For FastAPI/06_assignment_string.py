# String Assignment
# String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

# - Ask the user how many days until their birthday

# - Using the print()function. Print an approx. number of weeks until their birthday

# - 1 week is = to 7 days.


name = input("Enter you name: ")
brd = int(input("how many days before your brd: "))

rem = brd / 7

print(f"hi {name}. only {rem} weeks before your brd")

#round
print(round(rem, 2))  