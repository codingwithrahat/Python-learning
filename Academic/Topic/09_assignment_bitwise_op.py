#assignment operator

x = 5
x += 3  #8 (x = x + 3)

y = 10
y -= 4 #6 (y = y - 4)

z = 7
z *= 2 #14(z = z * 2)

a = 20
a /= 4 #5.0 (a = a/ 4)

b = 15
b %= 4  #3 (b = b % 4)

c = 17
c //= 3 #5 (c = c // 3)

d = 2
d **= 3 #8 (d = d ** 2)



print(x, y, z, a, b, c, d)




#2 bitwise operator


#and
a = 5 # In binary: 0101
b = 3 # In binary: 0011
result = a & b
print(result) #1 (0001)


#or
a = 5 # In binary: 0101
b = 3 # In binary: 0011
result = a | b
print(result) #7 (0111)

#xor

a = 5 # In binary: 0101
b = 3 # In binary: 0011
result = a ^ b
print(result)  #6 (0110)

#not
a = 5 # In binary: 0101
result = ~a
print(result) #-6 2s comp (a = -(a + 1))


#left shift
a = 3 # In binary: 0011
result = a << 2 #001100
print(result) #12

#right shift
a = 8 # In binary: 1000
result = a >> 2 #0010
print(result) #2
