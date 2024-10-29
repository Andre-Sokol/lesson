from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []  # локальный список
    with open(name, 'r', encoding = 'utf-8') as file: # Открывать файл name для чтения
        while True:
            line = file.readline() # Считывать информацию построчно
            all_data.append(line)
            if not line:
                break

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    # линейный подход
    start_L = datetime.now()
    for name in filenames:
        read_info(name)
    end_L = datetime.now()
    print(f'{end_L - start_L} (линейный)') # время выполнения линейный подход

    # многопроцессный подход
    start_M = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_M = datetime.now()
    print(f'{end_M - start_M} (многопроцессный)') # время выполнения многопроцессный подход