l = [1, 2, 3, 4, 6, 2, 3, 5, 4]

x = 4

idx = 0

for i in l:
    if(i == x):
        print("found at index : ", idx)
        break
    
    idx += 1

