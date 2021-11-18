number = int(input('Введите целое положительное число: '))
result = 0
while number != 0:
    ost = number % 10
    if ost > result:
        result = ost
    number = number // 10
print('Максимальное значение:', result)









