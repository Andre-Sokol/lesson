import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True
    # метод создания атрибута класса all_results
    # словарь в который будут сохраняться результаты всех тестов.
    @classmethod
    def setUpClass(self):
        self.all_results = {}

    # метод создания 3 участников
    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    # метод, где выводится результаты теста по очереди в столбец.
    @classmethod
    def tearDownClass(self):
        result = {}
        for k, v in self.all_results.items():
            result[k] = str(v.name)
            print(result)

    # метод 1- й тест между участниками 1 и 3
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_tournament1(self):
        tour = Tournament(90, self.runner1, self.runner3)
        Fin = tour.start()
        self.all_results.update(Fin)
        key = list(Fin.keys())[-1]
        self.assertTrue(Fin[key].__eq__('Ник'))

    # метод 2-й тест между участниками 2 и 3

    def test_tournament2(self):
        tour = Tournament(90, self.runner2, self.runner3)
        Fin = tour.start()
        self.all_results.update(Fin)
        key = list(Fin.keys())[-1]
        self.assertTrue(Fin[key].__eq__('Ник'))

    # метод 3- й тест между 3-мя  участниками 1, 2 и 3
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_tournament3(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        Fin = tour.start()
        self.all_results.update(Fin)
        key = list(Fin.keys())[-1]
        self.assertTrue(Fin[key].__eq__('Ник'))

    if __name__ == "__main__":
        unittest.main()
