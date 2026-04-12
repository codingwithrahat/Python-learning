name = "rahat"

print("hi " + name)


#string formating
print(f"hi {name}")

#another way
sen = "hi {}"
print(sen.format(name))

sen2 = "hi {} {}"
last_name = "hossan"
print(sen2.format(name, last_name))

print(f"hi {name} {last_name}. I hope you are learning")