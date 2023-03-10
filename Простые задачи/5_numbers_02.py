import random
#a = random.uniform(1001, 99999)
#b = random.uniform(1001, 99999)
a = 10083
b = 23000
c = a+b
#print(c)
def eqv(a, b, c):
    eps = max(a,b) * (0.0001)
    #print(eps)
    if eps == (c - eps):
        result = True
    else:
        result = False
    return result
print(eqv(a,b,c))

    
    
    
