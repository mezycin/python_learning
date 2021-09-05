start_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in start_list:
    name = list(i.split())[-1].capitalize()
    print(f'Привет, {name}!')