import abc
import random
import math

class IShape(abc.ABC):

    @abc.abstractmethod
    def get_perimeter(self):
        pass

    @abc.abstractmethod
    def get_area(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass


class Circle(IShape):
    PI = 3.14

    def __init__(self, radius):
        self.__radius = radius

    def get_perimeter(self):
        return math.floor(2 * self.__class__.PI * self.__radius)

    def get_area(self):
        return math.floor(self.__class__.PI * self.__radius ** 2)

    def get_description(self):
        print(f"Я - окружность с радиусом {self.__radius}")


class Rectangle(IShape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_perimeter(self):
        return (self.__length + self.__width) * 2

    def get_area(self):
        return self.__length * self.__width

    def get_description(self):
        print(f'Я - прямоугольник со сторонами {self.__length} и {self.__width}')


class Square(IShape):
    def __init__(self, side):
        self.__side = side

    def get_perimeter(self):
        return self.__side * 4

    def get_area(self):
        return self.__side ** 2

    def get_description(self):
        print(f'Я - квадрат со стороной {self.__side}')


class Game:
    question_count = 0

    def __init__(self):
        raise Exception("Нельзя создавать объекты данного класса")

    @staticmethod
    def __get_shape():
        n = random.randrange(3)
        if n == 0:
            return Circle(random.randrange(1, 20))
        if n == 1:
            return Rectangle(random.randrange(1, 20), random.randrange(1, 20))
        if n == 2:
            return Square(random.randrange(1, 20))

    @classmethod
    def __run(cls):
        question_count = cls.question_count
        while question_count:
            obj = cls.__get_shape()
            obj.get_description()
            if float(input("Назовите мою площадь(ответ округлите до целых в меньшую сторону): ")) == obj.get_area():
                print("Правильно!")
            else:
                print(f"Ошибка. Правильный ответ - {obj.get_area()}")
            if float(input("Назовите мой периметр(ответ округлите до целых в меньшую сторону): ")) == obj.get_perimeter():
                print("Правильно")
            else:
                print(f'Ошибка. Правильный ответ - {obj.get_perimeter()}')
            question_count -= 1
        if question_count == 0:
            if input("Продолжить игру? Y/N : ").upper() == "Y":
                cls.__run()
            else:
                print("Спасибо за участие")

    @classmethod
    def play(cls):
        cls.question_count = 2
        if input(f'Привет! Мы геометрические фигуры и у нас есть {cls.question_count} вопроса. Играем? \n Y/N : ').upper() == "Y":
            cls.__run()
        else:
            print("Спасибо за участие")


Game.play()












