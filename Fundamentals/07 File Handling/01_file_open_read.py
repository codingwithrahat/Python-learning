f = open("01_demo.txt", "r")  #by default mode "r" (read) and t (text mode)

data = f.read()

print(data)


data2 = f.read(5)  #only first 5 char 

print(data2)


#line by line

l1 = f.readline()
l2 = f.readline()

print(l1)
print(l2)

f.close()

