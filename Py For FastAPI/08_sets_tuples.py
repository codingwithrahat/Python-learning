"""
set
"""
#set is like list but unordered and no duplicate

s = {1, 2, 1, 2}
print(s)  #{1, 2}

print(len(s))  #2


#loop
for i in s:
    print(i)

# print(s[0])  we will get error , cz unordered

#remove
s.discard(1)
print(s)      #{2}

#clear all
s.clear()
print(s)   #set()


s.add(3) #not more then one element at a time
print(s)

#add more then one element
s.update([7, 7, 2])
print(s)




"""
tuples
"""
t = (1, 2, 3, 5, 1)
print(t)
print(len(t))
print(t[1])

# t[0] = 10 wil give error
#tuple can't add or update 

