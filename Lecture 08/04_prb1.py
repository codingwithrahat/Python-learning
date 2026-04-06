class stu:

    def __init__(self, name, mBan, mEng, mMath):
        self.name = name
        self.mBan = mBan
        self.mEng = mEng
        self.mMath = mMath

    def avg(self):
        a = (self.mBan + self.mEng + self.mMath) / 3
        return a
    

s1 = stu("Rahat", 99, 99, 98)
print(s1.avg())



# another way

class stu2:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    

    def avg(self):
        sum = 0

        for i in self.marks:
            sum += i

        return sum / 3

s2 = stu2("Rakib", [99, 99, 98])
print(s2.avg())