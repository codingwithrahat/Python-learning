#type validation

#name - str , age - int
def insert_data(name, age):
    print(name)
    print(age)


insert_data("rakib", "27") #here age is not int



# we can handle it - type hinding
def insert2_data(name : str, age : int):
    print(name)
    print(age)



insert2_data("rahat", 23) # here when another developer give value it show age : int
#but stil age can be any variable


#another way
def insert3_data(name : str, age : int):

    if(type(name) == str and type(age) == int):
        print(name)
        print(age)
    else:
        print("Wrong data type")


insert3_data("sarawer", 23) 



#data validation

def insert4_data(name : str, age : int):

    if(type(name) == str and type(age) == int):
        print(name)
        print(age)
    else:
        print("Wrong data type")


insert4_data("sarawer", -3) # age can't be negative

#way to solve this

def insert5_data(name : str, age : int):

    if(type(name) == str and type(age) == int):
        if age >= 0:
            print(name)
            print(age)
        else:
            print("invalid")
    else:
        print("Wrong data type")


insert5_data("sarawer", -3) 
#this is not suitable way

