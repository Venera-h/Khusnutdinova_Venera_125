import random
number = random.randint(1,101)
name = input("Введите ваше имя")
print("Привет!", name, " Я загадал число от 1 до 100, которое тебе нужно отгадать")

attempt = 0
while True:
    figure = int(input("Введите число"))
    attempt +=1

    if number>figure:
        print("Подсказка: число больше вашего ответа")
    if number<figure:
        print("Подсказка: число меньше вашего ответа")
    if number==figure:
        print("Ты угадал!")
        with open("game.txt","a") as f:
            f.write(f"\n{name}, ты угадал число за {attempt} попыток!.\n Правильное число - {number}\n")
            break