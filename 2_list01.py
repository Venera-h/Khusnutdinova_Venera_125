import random 
import collections
numbers_1 =[]
numbers_2 =[]
for i in range(50,101):
    numbers_1.append(random.randint(0,10000))
    numbers_2.append(random.randint(0,10000))
print(numbers_1)
print(numbers_2)
for j in numbers_2:
    if j in numbers_1:numbers_1.remove(j)
print(numbers_1)

#if collections.numbers_1 != collections.numbers_2:
#    numbers_3 = numbers_1
#print(n)


#def f(x1,y1):
 #   l = len(y1)
 #   for j in range(len(x1)):
  #      if x1[i:i+1] == y1:
 #           return print(x1[:i]+x1[i+l:])
        
#print(f([1,3,5,6,7,8,9],[1,2,3,4,5]))

    
