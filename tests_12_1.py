import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

    # Изменение значения в методе
    # def run(self):
    #     self.distance += 50

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        runner = Runner("John")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        runner = Runner("Denis")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, 'Неверное значение')

    def test_challenge(self):
        runner = Runner("Nina")
        runners = Runner("Alex")
        for i in range(10):
            runner.run()
        for i in range(10):
            runner.walk()
        self.assertNotEqual(runner.distance, runners.distance)

if __name__ == '__main__':
    unittest.main()
