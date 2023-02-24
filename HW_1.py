import math

def power(m2, r):
    G = 6.6743*(math.pow(10,-11))
    m1 = 5.97600 * math.pow(10,24)
    return (G*m1*m2)/(math.pow(r,2))

                      
print("Формула для расчета гравитации")
print("Выберите планету из списка: 1. Меркурий, 2. Венера, 3. Марс, 4. Юпитер, 5. Сатурн, 6.Уран, \
7. Нептун, 8. Плутон, 9. Луна 10. свой вариант")
n1 = int(input())
if n1 ==1:#Меркурий
    m2 = 3.302 * math.pow(10,23)
    r = 92 * math.pow(10,9)
    print("F = " + str(power(m2,r)))
    
if n1 ==2:# Венера (самая лучшая планета))
    m2 = 4.8685 * math.pow(10,24)
    r = 42 * math.pow(10,9)
    print("F = " + str(power(m2,r)))
    
if n1 ==3:# Марс
    m2 = 6.419 * math.pow(10,23)
    r = 79 * math.pow(10,9)
    print("F = " + str(power(m2,r)))
if n1 ==4:#Юпитер
    m2 = 1.8986 * math.pow(10,27)
    r = 628 * math.pow(10,9)
    print("F = " + str(power(m2,r)))
if n1 ==5:#Сатурн
    m2 = 5.6846 * math.pow(10,26)
    r = 1278 * math.pow(10,9)
    print("F = " + str(power(m2,r)))
if n1 ==6: #Уран
    m2 = 8.6832 * math.pow(10,25)
    r = 2721 * math.pow(10,9)
    print("F = " + str(power(m2,r)))
if n1 ==7:#Нептун
    m2 = 1.0243 * math.pow(10, 26)
    r =  4348 * math.pow(10,9)
    print("F = " + str(power(m2,r)))
if n1 ==8:#Плутон
    m2 = 1.31 * math.pow(10, 22)
    r =  6239 * math.pow(10,9)
    print("F = " + str(power(m2,r)))
if n1 ==9:#Луна
    m2 = 7.35 * math.pow(10, 22)
    r = 384399 * math.pow(10,3)
    print("F = " + str(power(m2,r)))
if n1 ==10:#cвой варик
    print("ведите значение массы без 10 умноженное в какой-то степени")
    m= int(input())
    print("Введите только степень 10")
    mst=int(input())
    m2= m*math.pow(10,mst)
    print("Введите растоояние между объектами")
    r = int(input())
    print("F = " + str(power(m2,r)))

print("PS учите физику;)")
