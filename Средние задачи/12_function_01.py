def sum_range(start, end):
    if start > end:
       start, end = end, start
    #start1 =end
    #end1 = start
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

start = int(input("Введите значение 1 :"))
end = int(input("Введите значение 2 :"))
print("Сумма = ", sum_range(start, end))