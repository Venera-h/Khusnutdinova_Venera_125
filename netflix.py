#Для упрощения жизни Х - Алиса, Y - Боб, Z - Чарли 
import random
cost = random.randint(400,1201)
friends = [X: random.randint(0,1501), Y: random.randint(0,1501), Z : random.randint(0,1501) ]

    X = random.randint(0,1501)
    Y = random.randint(0,1501)
    Z = random.randint(0,1501)

def netflix(cost, friends):
    moneysort = sorted(friends)
    almostcost= moneysort[0] + moneysort[1]
    if  moneysort[3] == X:
        print("Подписку может купить Боб и Чарли")
    elif  moneysort[3] == Y:
        print("Подписку может купить Алиса и Чарли")
    elif  moneysort[3] == Z:
        print("Подписку может купить Алиса и Боб ")

netflix(cost, friends)

#Для упрощения жизни Х - Алиса, Y - Боб, Z - Чарли 
import random
cost = random.randint(400,1201)
#friends = [X: random.randint(0,1501), Y: random.randint(0,1501), Z : random.randint(0,1501) ]

friends = {'X','Y','Z'}
X = random.randint(0,1501)
Y = random.randint(0,1501)
Z = random.randint(0,1501)

while (X+Y+Z)< cost:
    X = random.randint(0,1501)
    Y = random.randint(0,1501)
    Z = random.randint(0,1501)
    
def netflix(cost, X, Y, Z):
    moneysort = (X,Y,Z)
    moneysort = sorted(moneysort)
    almostcost= moneysort[0] + moneysort[1]
    if  moneysort[3] == 'X':
        print("Подписку может купить Боб и Чарли")
    elif  moneysort[3] == Y:
        print("Подписку может купить Алиса и Чарли")
    elif  moneysort[3] == Z:
        print("Подписку может купить Алиса и Боб ")

netflix(cost, X, Y, Z)






    


