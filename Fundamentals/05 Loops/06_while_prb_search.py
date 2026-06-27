#search a number in a tuple

t = (1, 3, 4, 6, 7 , 8, 2, 7 ,7, 8)

x = 7

i = 0

while i < len(t):
    if (t[i] == x):
        print("fount at index :", i)
        break
    else:
        print("Finding...")
    i+=1

