import math


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides: int, filled: bool = True):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):  # возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, r, g, b):  # проверяет корректность переданных значений перед установкой нового цвета.
        if r % 1 == 0 and g % 1 == 0 and b % 1 == 0 and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g,
                  b):  # изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        number_of_new_parties = []
        for i in sides:
            if i > 0:
                number_of_new_parties.append(i)
        if len(number_of_new_parties) > 0 and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def get_sides(self): #  должен возвращать значение я атрибута __sides.
        return self.__sides

    def __len__(self): # должен возвращать периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):          # должен принимать новые стороны, если их количество не равно sides_count,
        if self.__is_valid_sides(new_sides):  # то не изменять, в противном случае - менять.
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __radius(self):                        # рассчитать исходя из длины окружности
        return self.__len__ * (2 / pi)

    def get_square(self):                      # возвращает площадь круга
        return (self.__len__ ** 2) / (4 * pi)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):                       # возвращает площадь треугольника.
        p = self.__len__ / 2
        S = math.sqrt((p(p - self.__sides[0])(p - self.__sides[1])(p - self.__sides[2])))
        return S


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides: int, filled: bool = True):
        super().__init__(color, sides)
        self.__sides = sides
        if len(self.__sides) != 1:
            sides = [1]
        self.__sides = sides * self.sides_count  # Переопределить __sides сделав список из 12 одинаковых сторон

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return self.__sides[1] ** 3  # возвращает объём куба.


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# # Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# Проверка объёма (куба):
print(cube1.get_volume())
#









