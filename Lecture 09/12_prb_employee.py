class emp:
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def show(self):
        print("Role :", self.role, "Dept :", self.dept, "Salary :", self.sal)

class eng(emp):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("SWE", "IT", 2000000)

    


e1 = eng("rahat", 23)
e1.show()

