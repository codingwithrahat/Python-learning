#1
#many value to multiple variable

x, y = 'Rahat', 'Hossan'

print(x, y)




#2
#one value to multiple varibale

x = y = 'Rahat Hossan'

print(x, y)




#3
# a string in python is a object of str class

type("Rahat")




#4 Tuple

type(('Rahat', 2)) #tuple
#list or array and tuple are both same, just list use [ ] and tuple use ( )

t = ('Rahat', 3)
print(t[0])
# t[0] = 'Rakib'
# this line will give error , cz tuple can't be updated

l = ['Rahat', 3]
l[0] = 'Rakib' #list can be update later
print(l[0])





#5 Range
# range is an built in fcuntion
#range(star, stop, step)

#star by default 0
#stop mandotary 
#step by default 1 (increment by 1)

for i in range(5):
  print(i) # 0 1 2 3 4

for i in range(1, 5):
  print(i) # 1 2 3 4

for i in range(1, 5, 2):
  print(i) # 1 3



