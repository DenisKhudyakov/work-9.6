# Задание 2

text = input('Введите текст: ')
sumbol = '*'
number = 0
print('Символ «*» стоит на позиции', text.index(sumbol))

#Альтернативное решение данной задачки через цикл и счетчик

for i in text:
    if i.__eq__('*'):
        print('Символ «*» стоит на позиции', number)
    number += 1



