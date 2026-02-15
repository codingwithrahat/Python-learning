stu = {
    "name" : "rahat",
    "sub" : {
        "phy" : 20,
        "che" : 30
    }
}

#keys and values 

#return in list form with dict_keys[]
print(stu.keys())   
print(stu.values()) 


#print in only list form
print(list(stu.keys()))  #remove dict_keys(), only[]

print(len(list(stu.keys())))  #length of keys list



#items

print(stu.items()) #return as pair in tuple

print(list(stu.items())) #remove dict_items()

p = list(stu.items())

print(p[0]) #first pair, to use this must type cast in list





#get

print(stu.get("name"))

print(stu.get("name2")) #print None, cz nam2 is not exists
# print(stu["name2"]) will give error , cz name2 is not exists




#update
stu.update({"city" : "Dhaka"}) 

new_dict = {"name":"Rakib", "car" : "bmw", "hair" : "black"} 
stu.update(new_dict) 

print(stu)

