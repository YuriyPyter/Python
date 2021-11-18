revenue = int(input('Введите значение выручки фирмы: '))
cost = int(input('Введите значение издержек фирмы: '))
profit = revenue - cost    # прибыль
loss = cost - revenue      # убыток
profitability = profit / revenue   # рентабельность
if revenue > cost :
    print('Ваша прибыль составляет:', profit)
    print('Рентабельность фирмы:', profitability)
    quantity_people = int(input('Введите численность сотрудников фирмы:'))
    profit_one = profit / quantity_people   # прибыль, в расчёте на одного сотрудника
    print('Прибыль фирмы в расчёте на одного сотрудника:', profit_one)
elif revenue < cost:
    print('Ваш убыток составляет:', loss)

