from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        numbers = range(1, word_count + 1)
        for number in numbers:
            file.write(f'Какое-то слово № {number}' + '\n')  # запись слов "Какое-то слово № <номер слова по порядку>"
            sleep(0.1)  # в соответствующий файл
    print(f'Завершилась запись в файл{file_name}')


time_start = datetime.now()  # время начала работы функций

# вызов 4 раза функциb write_words

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_stop = datetime.now()  # время окончания работы функций
time_res = time_stop - time_start  # затраченое время на работу функций

print(f'Время выполнения функций {time_res}')

time1_start = datetime.now()  # время начала работы потока

# Создание и запуск потоков
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourh = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourh.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourh.join()

time1_stop = datetime.now()  # время окончания работы потока
time1_res = time1_stop - time1_start  # затраченое время на работу потока
print(f'Время работы потоков {time1_res}')
