#methods means function
#funtions are same for list and string
#but methods are spechific , like list specific methods

l = [2, 1, 3]

#append
l.append(4)
l.append(5)    #as like push_back()

print(l)

#sort
l.sort()       #ascending order , it return NONE , it directly sort the function

print(l) 

#sort in desending
l.sort(reverse = True) #desending order

print(l)

#reverse
l.reverse() 

print(l)

#insert
l.insert(1, 10)   #as like l[1] = 10

print(l[1])  #10


#remove
l.remove(10) #remove value 10, first occurrence of value
print(l)

#pop
l.pop(0) #remove index 0, value 1
print(l)

#copy
l2 = l.copy()
print(l2)


