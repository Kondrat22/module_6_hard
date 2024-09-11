import math


class Figure:
    sides_count = 0
    filled = False

    def __init__(self, __color, __sides):

        self.__color = __color
        self.__sides = __sides

    def get_color(self):
        r = self.__color[0]
        g = self.__color[1]
        b = self.__color[2]
        return [r, g, b]

    def __is_valid_color(self, r, g, b):
        correct_colors = True
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            correct_colors = False
        return correct_colors

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):

        num_sides = len(sides)

        if num_sides == self.sides_count:
            for i in range(0, num_sides):
                if type(sides[i]) != int or sides[i] < 0:
                    return False
        else:
            return True
        self.__sides = sides[0]
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimeter = 0
        for i in range(0, len(self.__sides)):
            perimeter += self.__sides[i]
        return perimeter

    def set_sides(self, *new_sides):
        side_list = []
        if self.__is_valid_sides(*new_sides):
            for i in range(0, self.sides_count):
                side_list.append(self.__sides)

            self.__sides = side_list


class Circle(Figure):
    sides_count = 1
    __radius = 1 / (2 * math.pi)

    def get_square(self):
        self.__radius = (self.__len__()) / (2 * math.pi)
        return math.pi * pow(self.__radius, 2)


class Triangle(Figure):
    sides_count = 3
    __height = 1
    __base = 1

    def get_square(self):
        h_p = self.__len__() / 2
        __height = 2 * math.sqrt(
            (h_p * (h_p - self.__sides[0]) * (h_p - self.__sides[1]) * (h_p - self.__sides[2])) / 2)

        return 0.5 * self.__height * self.__base


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        self.__sides = self.get_sides()
        vl = pow(self.__sides[0], 3)
        return vl


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

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
