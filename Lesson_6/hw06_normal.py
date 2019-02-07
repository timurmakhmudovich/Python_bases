'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''

from math import sqrt

class Triangle:
    def __init__(self, A, B, C):
        self.a = A
        self.b = B
        self.c = C
        self.__ac = sqrt((self.a[0] - self.c[0]) ** 2 + (self.a[1] - self.c[1]) ** 2)

    def length(self, a, b):
        return sqrt((a[0] - b[0])** 2 + (a[1] - b[1])**2)

    @property
    def p(self):
        return self.length(self.a, self.b) + self.length(self.a, self.c) + self.length(self.b, self.c)

    @property
    def h(self):
        p = self.p / 2
        ab = sqrt((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2)
        bc = sqrt((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2)
        return sqrt(p * (p - self.__ac) * (p - ab) * (p - bc)) * 2/ self.__ac

    @property
    def s(self):
        return self.__ac * self.h / 2


A = (1, 1)
B = (3, 3)
C = (5, 1)

triangle = Triangle(A, B, C)

print(f"Периметр треугольника: {triangle.p}")
print(f"Высота, опущенная на сторону AC: {triangle.h}")
print(f"Площадь треугольника: {triangle.s}")

