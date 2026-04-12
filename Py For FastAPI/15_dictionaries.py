d = {
    "username" : "rahat",
    "name" : "rahat hossan"
}

print(d)
print(d.get("name"))

d["married"] = False

print(len(d))


#remove by key
d.pop("username")
print(d)

d.clear()
print(d)

# del d , also work


d = {
    "username" : "rahat",
    "name" : "rahat hossan"
}

#both are same
for i in d:
    print(i)  #only get the keys
for i in d.keys():
    print(i)  #only get the keys


for i in d.values():
    print(i)  #only get the values

for i in d.items():
    print(i)  #get the keys and values with ()

for i, j in d.items():
    print(i, j)  #without ()



#this is not a perfect way of copy
d2 = d
d2.pop("name")
print(d.get("name"))  #name is also remove from d

#perfect way to copy
d3 = d.copy()
d3.pop("username")
print(d.get("username"))  #username will not remove from d