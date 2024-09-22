class Horse:
    x_distance = 0  # пройденный путь.
    sound = 'Frrr'  # звук, который издаёт лошадь.

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    y_distance = 0  # высота полёта
    sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    sound = 'I train, eat, sleep, and repeat'  # так как у класса Pegasus преоритет выше, иначе Pegasus издаёт звук Frrr

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(f'{self.sound}')


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
