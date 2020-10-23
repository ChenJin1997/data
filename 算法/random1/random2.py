import random
def randomList(len:int,max:int)->list:
    nums = []
    for i in range(len):
        nums.append(random.randint(1,max))
    return nums
