# Задание 3

row = int(input('Введите количество рядов: '))
seat = int(input('Введите количество сидений: '))
metres = int(input('Введите количество метров между рядами: '))
print('Сцена\n')
for i in range(row):
    for j in range(seat):
        print('=',end='')
    print(' ', end= '')
    print('*'*metres, end=' ')
    print('',end='')
    print('='*seat,end= '')
    print()


