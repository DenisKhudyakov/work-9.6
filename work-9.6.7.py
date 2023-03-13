# Задание №7


word = input('Введите зашифрованое слово: ')
sum1 = ''
sum2 = ''
count = 0

for i in word:
    count += 1
    if (count % 2 == 1):
        sum1 += i
for i in  reversed(word):
    count += 1
    if count % 2 == 1:
        sum2 += i

print('Расшифрованое слово', sum1 + sum2)