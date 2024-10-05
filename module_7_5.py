import os
import time

for root, dirs, files in os.walk('.'):
    for file in files:
        if os.path.isfile(file):
            filepath = os.path.join(root, file) # путь к файлу
            filetime = os.path.getmtime(file)   # время изменения, число с плавающей запятой, указывающее количество секунд с начала эпохи Unix
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.stat(file).st_size    # размер файла
            parent_dir = os.path.dirname(filepath)  # родительский каталог

            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
                  f' {formatted_time}, Родительская директория: {parent_dir}')
