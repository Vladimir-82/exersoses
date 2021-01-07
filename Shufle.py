import random
a = [1, 5, 6, 9]
random.shuffle(a)
gen=(i for i in a)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))