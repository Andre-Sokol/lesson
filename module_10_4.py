from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number  # номер стола
        self.guest = guest  # гость, который сидит за этим столом


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name  # имя гостя

    def run(self):
        sleep(randint(3, 10))  # задержка


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # очередь гостей
        self.tables = tables  # список столов

    # добавление гостя в очередь
    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(а) за стол номер {table.number} ')
                    self.thread = Guest(guest.name)
                    self.thread.start()
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди.')

    # обсуждение гостей
    def discuss_guests(self):
        while self.queue.empty() is True or Cafe.table_control(self):
            for table in self.tables:
                if not (table.guest is None) and self.thread.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not (self.queue.empty()) and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    self.thread2 = Guest(table.guest.name)
                    self.thread2.start()
    # занятость столов
    def table_control(self):
        for table in self.tables:
            if table is not None:
                return True
            else:
                return False


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()