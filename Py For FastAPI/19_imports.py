# manual import from another file

#funciton in file f
def cal_hw(hw):
    sum = 0

    for i in hw.values():
        sum += i
    
    final_grade = round(sum / len(hw), 2)
    print(final_grade)

# from f import cal_hw
# if function cal_hw in a file name "f"

homeWork = {
    "hw1" : 85,
    "hw2" : 100,
    "hw3" : 81
}

cal_hw(homeWork)




#strandard library 

import random
drinks = ['soda', 'water', 'tea']
print(random.choice(drinks))  #every time it gives a random elements form drinks\

print(random.randint(1, 10))

import math
s = math.sqrt(64)
print(s)