#set is mutable but element of set is immutable (elements can't change)
#thats wgy set can't store list and dict , cz they are mutable

st = {1, 2, "rahat"}   #unordered

print(type(st))

print(st)


st = {1, 2, 1, 2}   #ignore dublicate

print(len(st))  #2



# st = {}, this is not an empty set it is a dict

#empty set

st = set()

print(st)