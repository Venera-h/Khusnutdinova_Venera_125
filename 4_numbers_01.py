import random 
numbers_1 =[]
result = False
for i in range(5,101):
    numbers_1.append(random.randint(0,10000))
X = random.randint(1,10000) #по идеи мы не можем ограничивать число Х,
# ведь оно по условию должно быть  >0 
sum = 0
for j in numbers_1:
    sum= sum + j
    
def magic(sum, X):
    if sum% X ==0:
        result = 1
        print("Делится")
    else:
        result = 0
        print("Нельзя делить без остатка")


print("X =" + str(X))
print("sum =" + str(sum))
magic(sum, X)
print(result)
