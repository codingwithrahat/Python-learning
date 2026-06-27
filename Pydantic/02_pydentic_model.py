from pydantic import BaseModel

class patient(BaseModel):
    name : str
    age : int


def data(pat : patient):
    print(pat.name)
    print(pat.age)


pat_info = {"name" : "Rakib", "age" : 27}

p1 = patient(**pat_info)

data(p1)