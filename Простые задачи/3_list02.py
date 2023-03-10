import random 
numbers_1 =[]
numbers_2 =[]
for i in range(50,101):
    numbers_1.append(random.randint(0,10000))
    numbers_2.append(random.randint(0,10000))
print(sorted(numbers_1))
print(sorted(numbers_2))
numbers_3 = list(set(numbers_1 + numbers_2))
print(sorted(numbers_3))