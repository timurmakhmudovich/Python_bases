'''
Задание_1. Создать класс. В конструктор передать два параметра - два числа.
Создать второй класс. В конструкторе первого предусмотреть создание
объекта второго класса. Кроме того, в первом классе предусмотреть три метода,
в которых делегировать получение остатка от деления, результата деления и целой
части от деления в методы второго класса (предусмотреть вычисление в соотв. методах
второго класса).
'''


class First:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = Second(a, b)

    def __getattr__(self, attrname):
        return getattr(self.c, attrname)



class Second:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def div(self):
        return self.a / self.b

    def intdiv(self):
        return self.a // self.b

    def moddiv(self):
        return self.a % self.b


data = First(20,3)
print(data.div())
print(data.intdiv())
print(data.moddiv())
