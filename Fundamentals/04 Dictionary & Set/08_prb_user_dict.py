#take a empty dict , take 3 subject mark form user

d = {}

phy = int(input("Phy mark : "))
che = int(input("Che mark : "))
mat = int(input("Mat mark : "))


d["Phy"] = phy
d.update({"Che" : che})
d["Mat"] = mat

print(d)