#1 Dictonaries
#like hash table
#{key, value}

dict ={}

dict[1] = 'One'
dict[2] = 'Two'
dict['Three'] = 3 

print(dict)  


d = {'name' : 'Rahat', 'Roll' : 32}

print(d)              #print complete dict
print(d['name'])      #print value for key 'name'
print(d.keys())       #print all keys
print(d.values())     #print all values

type(d)               # type - dict






#2 type casting

x = 1           #by default int
y = int(1.4)    #it will be 1
z = int('3')    #it will be 3(int)

w = float(1)    #it will be 1.0
o = float("3")  #it will be 3.0

a = str(1)      #it will be '1' or "1"

print(x, y, z, w, o, a)
type(a)         #str
