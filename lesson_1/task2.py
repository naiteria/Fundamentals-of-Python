n = int(input('Введите некоторое количество секунд, а программа переведет это количество в привычный формат '
              '"чч:мм:сс": '))
hours = n // 3600
minutes = (n - (hours * 3600)) // 60
seconds = n - ((hours * 3600) + (minutes * 60))
print(f'Время в привычном формате "чч:мм:сс": {hours} : {minutes} : {seconds}')
