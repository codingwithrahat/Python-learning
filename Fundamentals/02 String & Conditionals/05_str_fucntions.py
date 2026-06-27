str = "Rahat Hossan"

print(str.endswith("an"))  #return type fuinction, True


str2 = "rakib"
print(str2.capitalize())  #Rakib
print(str2)               #rakib

# for permanent solution

str3 = str2.capitalize()

print(str3)               #Rakib


#for update char in string
print(str3.replace("Ra", "aa"))  #aakib
print(str3)                      #Rakib


print(str3.find("k"))  #index of k
print(str3.find("akib"))  #index of a
print(str3.find("r"))  #index -1, not exists

print(str3.count("a"))

