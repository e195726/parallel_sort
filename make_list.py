import random
def make(number):
    numlist =[]
    for i in range(number):
        numlist.append(random.randint(0,1000))
    return numlist

