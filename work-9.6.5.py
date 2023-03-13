# задание №5

text = input('Введите текст: ')
word = ''
max_len = 0
for i in text:
    if i == ' ' or i == '.':
        word = ''
        continue
    word += i
    if len(word) > max_len:
        max_len = len(word)

print('Самое длинное слово:', max_len, 'букв')