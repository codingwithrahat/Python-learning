# Functions Assignment
# - Create a function that takes in 3 parameters(firstname, lastname, age) and

# returns a dictionary based on those values

def f(fname, lname, age):
    d = {
        "FirstName" : fname,
        "LastName" : lname,
        "Age" : age
    }

    return d

d = f("Rahat", "Hossan", 23)
print(d)