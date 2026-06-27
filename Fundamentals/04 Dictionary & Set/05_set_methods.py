st = set()

#add

st.add(1)
st.add("Rahat")

#set can't store dict and list
# but it can store tuple 
st.add((1, 2, 3))

print(st)


#remove
st.remove("Rahat")

print(st)



#pop
#it remove random value
st.pop()

print(st)



#clear
st.clear()
print(len(st))




#union
#as like math set union 

st1 = {1, 2, 3}
st2 = {3, 4, 5}

print(st1.union(st2))  #union fucntion return e new set



#intersection
st3 = st1.intersection(st2)

print(st3)







