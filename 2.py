time = int(input('Введите время в секундах: '))
hour = time // 3600
minute = (time % 3600) // 60
second = (time % 3600) % 60
print(f'Время: {hour:02} чч {minute:02} мм {second:02} cc')
print(f'{hour:.2f}')

