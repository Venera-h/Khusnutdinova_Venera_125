import random 
import collections
numbers_1 =[]
numbers_2 =[]
numbers_3 = []
for i in range(50,101):
    numbers_1.append(random.randint(0,10000))
    numbers_2.append(random.randint(0,10000))
print(numbers_1)
print(numbers_2)
numbers_3 = [j for j in numbers_1 if j in numbers_2]
print(numbers_3)
