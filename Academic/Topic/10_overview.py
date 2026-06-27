#1
print("SEU")
print("Rahat")

#2
a = 2
type(a) #print int

#3
a = 5.0
type(a)
print(a) #print 5.0

#4
b = 2
print(b * 5) #print 10

#5
n = float(input("Enter Number")) #take user input
print(n)

n = float(input("Enter number 1: "))
o = input("Enter Operator: ")
m = float(input("Enter number 2: "))


#6
if o == '+':
  print(n+m)
elif o == '-':               #elif works like else if
  print(n - m)
else:
  print("Enter Correct Operator")


#7
i = 1

while i<3:
  print(i)
  i += 1       #i++ isn't support

#8
a = "Rahat"
b = 'Rahat'   #both "" & '' are work perfect
print(a)
print(b)


#9
a = "Rahat Hossan"
print(a[1:4])         ## slice from index 1 to 3
print(a.lower())      #make all character lowercase
print(a.upper())      #make all character uppercase 


#10
a = 2
b = 3

if a>b:
  print("a > b")
else:
  print("a < b")


#11
import statistics
data = [1, 2, 9, 5, 6]

x = statistics.mean(data)
y = statistics.median(data)
z = statistics.stdev(data)
w = statistics.variance(data)

print(x)
print(y)
print(z)
print(w)

#12
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

from google.colab import files
files.upload()                        #can upload file from my pc, files.upload() works only in Google Colab

#13
df = pd.read_excel('c1.xlsx')
df                                 #show the excell file that i uploaded

#14
plt.xlabel('Area')
plt.ylabel('Price')

plt.scatter(df.Area, df.Price, color = 'blue', marker = '*')     #show a graph of my given data, that i store in the excell sheet
