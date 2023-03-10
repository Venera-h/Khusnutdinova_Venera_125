#Для упрощения жизни Х - Алиса, Y - Боб, Z - Чарли 
import random
cost = random.randint(400,1201)
#friends = [X: random.randint(0,1501), Y: random.randint(0,1501), Z : random.randint(0,1501) ]

X = random.randint(0,1501)
Y = random.randint(0,1501)
Z = random.randint(0,1501)

def netflix(cost, X, Y, Z):
    if X+Y+Z > cost:
        #max_money = max(X,Y,Z)
        min_money = min(X,Y,Z)
        if min_money==X:
            print("Подписку может купить Боб и Чарли")
        elif  min_money == Y:
            print("Подписку может купить Алиса и Чарли")
        elif  min_money == Z:
            print("Подписку может купить Алиса и Боб ")

netflix(cost, X, Y,Z)



    


