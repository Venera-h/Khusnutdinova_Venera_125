nick = (str(input("Введите свой ник\n")))
good_nick = ['Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг', 'Клодобродыч']
def evil(nick):
    if nick in good_nick:
        print("Ты – свой. Приветствую, любезный", nick)
    else:
        print("Тут ничего нет. Еще есть вопросы?")

evil(nick)