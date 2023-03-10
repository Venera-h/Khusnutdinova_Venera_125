
subst = str(input('Напишите любой текст'))
st = str(input('Напишите любой текст'))
def search_substr(subst, st):
    if subst.lower().find(st.lower()) != -1:
        print("Есть контакт!")
    else:
        print("Мимо!")

search_substr(subst, st)