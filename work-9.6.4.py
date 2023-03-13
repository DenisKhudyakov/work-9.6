#Задание 4
for _ in range(15):
    i = 8
    j = 10
    for z in range(20):
        command = input('Введите команду: ')
        if command.__eq__('w'):
            i += 1
            if i > 15:
                continue
        elif command.__eq__('a'):
            j -= 1
            if j < 0:
                continue
        elif command.__eq__('s'):
            i -= 1
            if i < 0:
                continue
        elif command.__eq__('d'):
            j += 1
            if j > 20:
                continue
        print('Марсоход находится на позиции', i, j, end=' ')
