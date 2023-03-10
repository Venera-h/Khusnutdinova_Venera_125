stroka = str(input())
def register(stroka):
    new_register= ""
    num = 0
    stroka = stroka.lower()
    for i in stroka:
        if num%2 ==0:
            num += 1
            new_register += i.upper()
        else:
            num+=1
            new_register += i.lower()

    return(new_register)

print(register(stroka))




