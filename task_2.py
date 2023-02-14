seconds = int(input("Введите время в секундах: "))
hour = seconds / 3600
minutes = seconds / 60
print(f'Время в формате ч:м:с - {float(hour)} : {float(minutes)} : {seconds}')