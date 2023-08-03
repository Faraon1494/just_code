import random
print(random.random())
print(random.randint(1,10))
print(random.randrange(1,10,2))
ls=[1,2,3,4,5,6]
random.shuffle(ls)
print(ls)
print(random.choice(ls))