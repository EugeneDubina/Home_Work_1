revenue = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
if revenue > costs:
    print(f'Фирма работает с прибылью.')
    profit = revenue - costs
    rent = profit / revenue
    print(f'Рентабельность = {rent}')
    works = int(input("Введите численность сотрудников: "))
    work_profit = profit / works
    print(f'Прибыль фирмы в расчете на одного сотрудника = {float(work_profit)}')
elif revenue == costs:
    print('Фирма работает в ноль')
else:
    print('Фирма работает в убыток')