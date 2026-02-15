info = {
    "key" : "value",
    "name" : "Rahat",
    "age" : 21,
    "subject" : ["ENG", "CSE"],
    "topic" : ("dict", "set")
}

#tuple can be also a key but list can't
#can tuple is immuated and list is mutted

print(type(info))
print(info)

#dict is unorder, there is no index serial
#dict is mutable
#duplicate key not possible

print(info["name"])

#update value
info["name"] = "Rahat Hossan"

print(info["name"])

#update new key with value

info["Hobby"] = "Coding"

print(info["Hobby"])

print(info)

#null dict
dict2 = {}
print(dict2)