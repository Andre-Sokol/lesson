from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name  # имя рыцаря
        self.power = power  # сила рыцаря

    def run(self):
        enemies = 100
        number_of_days = 0
        print(f"{self.name}, на нас напали!")
        while enemies > 0:  # Рыцарь сражается до тех пор, пока не повергнет всех врагов
            enemies -= self.power  # В процессе сражения количество врагов уменьшается на power текущего рыцаря
            number_of_days += 1
            sleep(1)
            print(f'{self.name} сражается {number_of_days} дней ..., осталось {enemies} войнов.')
        print(f'{self.name} одержал победу спустя {number_of_days} дней(дня)!')



# Создайте и запустите 2 потока на основе класса Knight.
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')