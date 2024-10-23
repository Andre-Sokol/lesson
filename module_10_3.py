import threading
from time import sleep
from random import randint


class Bank():
    def __init__(self):
        super().__init__()
        self.balance = 0  # баланс банка
        self.lock = threading.Lock()  # блокировка потоков

    def deposit(self):
        transactions = 0
        while transactions < 100:  # совершать 100 транзакций пополнения средств
            transactions += 1
            n = randint(50, 500)
            self.balance += n  # Пополнение баланса
            print(f'Пополнение: {n}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
        sleep(0.001)

    def take(self):
        transactions = 0
        while transactions < 100:  # совершать 100 транзакций снятия средств
            transactions += 1
            n = randint(50, 500)
            print(f'Запрос на {n}')
            if n <= self.balance:
                self.balance -= n  # Снятие средств
                print(f'Снятие: {n}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
