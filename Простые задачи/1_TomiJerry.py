print(" Введите скорость Джерри в м/с")
print("Для справки: чтобы перевести из км\ч в м\с нужно делить на 3.6")
X = int(input())
print(" Введите скорость Тома в м/с")
Y = int(input())
print("Введите расстояние между ними в метрах")
S = int(input())
if Y<X: print("Джери смог оторваться")
else:
    t = (Y-X)/ S
    print("Том догонит джери за " + str(t)+"с")
