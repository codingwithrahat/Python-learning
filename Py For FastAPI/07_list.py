l = [2, 3, 14, 5, 16]
print(l)

p = ["Rahat", "rakib"]
print(p)


print(l[0])
p[1] = "sarawer"
print(p[1])

print(len(p))


#slicing
print(l[1:3])  #index 1, 2

#add in last like push_back
p.append("rakib")
print(p)


#add in index
p.insert(2, "hossan")
print(p)

#remove
p.remove("sarawer")
print(p)

#remove index
p.pop(2)
print(p)


l.sort()
print(l)