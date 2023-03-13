#Задание 1
count = 0
for i in range(10):
    text = input('Ввдите слово: ')
    if text.__eq__('Карамба'):
        print('Добро пожаловать на борт')
        count += 1
    else:
        print('За борт его')
print('Экипаж', count, 'матросов')