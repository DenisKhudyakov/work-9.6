# Задание №6
command = input('Введите команду в формате "ab" из 10 символов: ')
sum_milk = 0
for i in command:
    if i.__eq__('a'):
        continue
    elif i.__eq__('b'):
        sum_milk += 2
print('Выработка молока в сутки равна', sum_milk)