#1
print(5**2) 

"""
5^2 another style of cmnt
"""



#2
x = str(3) #x will be asign as string
y = int(3) #y will be integer , bt dafault
z = float(3) #z will be 3.0

print(x, y, z)



#3
x = str(3)

# print(x + 2) will give error

print(x + "2")



#4
x = "Rahat"
y = 'Rahat'

#work as same

print(x, y)



#5
#varaible are case sensitive
b = 5
B = 6

print(b, B) # b and B are diff



#6 string
s = "Rahat Hossan"

print(s)            #print complete string
print(s[0])         #print first char of the string
print(s[2:5])       #print char from index 2 to index 4 (0 based index)
print(s[2:])        #print from index 2 to end
print(s * 2)        #print string 2 times(as like add two string)
print(s + "Rahat")  #print string s then add "Rahat"

# plus sign (+) is string concetanation opearator
# asterisk sign (*) is python repetation opeartor



#7 list or array
list = ['Rahat', 2, 3.4, "Hossan"]
a = ['Rakib', 2]

print(list)           #print complete array
print(list[0])        #print first element
print(list[2:4])      #print from index 2 to index 3 (0 based index)
print(list[2:])       #print from index 2 to end
print(a * 2)          #print array a two times
print(list + a)       #add both array
