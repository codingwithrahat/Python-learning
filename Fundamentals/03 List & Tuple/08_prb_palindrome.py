#list contains palindrome or not

l = [1, 2, 3, 2, 1]

l2 = l.copy()

l2.reverse()

if(l == l2):
    print("YES")
else: 
    print("NO")