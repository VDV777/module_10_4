# Необходимо имитировать ситуацию с посещением гостями кафе.
# Создайте 3 класса: Table, Guest и Cafe.
# Класс Table:
# Объекты этого класса должны создаваться следующим способом - Table(1)
# Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
# Класс Guest:
# Должен наследоваться от класса Thread (быть потоком).
# Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
# Обладать атрибутом name - имя гостя.
# Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
# Класс Cafe:
# Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
# Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
# Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
# Метод guest_arrival(self, *guests):
# Должен принимать неограниченное кол-во гостей (объектов класса Guest).
# Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
# Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
# Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
# Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
# Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
# Далее запустить поток этого гостя (start)
# Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
# Table - стол, хранит информацию о находящемся за ним гостем (Guest).
# Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
# Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
import random
import time
from queue import Queue
from threading import Thread


class Table:

    def __init__(self, number: int):

        self.number: int = number
        self.guest: Guest = None


class Guest(Thread):

    def __init__(self, guest: str):
        super().__init__()

        self.guest: str = guest

    def run(self):

        time.sleep(random.randint(3, 10))


class Cafe:

    def __init__(self, tables: list[Table]):

        self.queue = Queue()
        self.tables: list[Table] = tables

    def guest_arrival(self, guests: list[Guest]):

        for guest in guests:

            table_test: Table = Table(-1)

            for table in self.tables:

                if table.guest is None:
                    table.guest = guest
                    table_test = table
                    break

            if table_test.guest is None:
                print(f'{guest.guest} в очереди')
                self.queue.put(guest)
            else:
                print(f'{guest.guest} сел(-а) за стол номер {table_test.number}')
                guest.start()

    def discuss_guests(self):

        while not self.queue.empty():

            for table in self.tables:

                if not table.guest.is_alive():
                    print(f'{table.guest.guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')

                    guest: Guest = self.queue.get()
                    table.guest = guest
                    guest.start()
                    print(f'{guest.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

                    break

            if any(self.tables.)








# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(tables)
cafe.guest_arrival(guests)

cafe.discuss_guests()