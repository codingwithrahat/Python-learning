input() 
#take a input

input("Enter your name : ")

age = input("Enter your age : ")  

print(age)
print(type(age)) #str, by default input will be str


#need type casting
age = int(input("Enter your age : ")) #input will be int 
print(type(age)) #int