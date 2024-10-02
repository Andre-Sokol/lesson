import io
from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, j in enumerate(strings, start=1):
            key = (i, file.tell())               # формируем ключь где i - № строки, а file.tell() - байт начал строки
            strings_positions.update({key: j})   # формируем словарь ключь = значение (строка)
            file.write(f'\n{str(j)}')            # запись в файл
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
