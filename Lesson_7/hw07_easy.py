'''
Задача-1: Реализовать индексацию элементов списка не с нуля, а с 5, т.е. 5, 6, 7
и т.д.
'''

class MyList(list):
    def __getitem__(self, offset):
        return list.__getitem__(self, offset - 5)


lst = MyList([1,2,3,4,5,6,7,8,9])
print(lst[5])

'''
Задача-2: Придумать любу структуру данных. Она должна содержать два атрибута.
Значение одного атрибута передается в конструктор, а значение другого - определяетсяъ
прямо в конструкторе класса. Для этой структуры данных написать метод,
который должен выполнять какой-то функционал. Создать экземпляр класса, передать
данные. Вызывать метод. Проверить, что находится в переменной-экземпляре класса.
Переопределить метод __str__. Этот метод должен возвращать тот результат,
который вы захотите. Проверить еще раз. В комментарии написать, в чем разница
между подходом с использованием метода __str__ и без него.
'''
#возвращает двоичный код числа, поделенного на 2
class MyClass:
    def __init__(self, number):
        self.divider = 2
        self.number = int(number)

    def binary(self):
        return bin(self.number//self.divider)

    def __str__(self):
        return f"Результат целочисленного деления числа {self.number} на {self.divider}  - {self.binary()}"


a = MyClass(11.999)
b = a.binary()
c = str(a)

print(b)
print(c)

'''
Задача-3: Продолжить работу над задачей 2. Добавить еще один метод. Он должен
вывзваться из экземпляра класса. В этот метод нужно передать некое значение.
Сам метод должен ловить значение и что-то с ним делать и возвращать результат.
Реализовать для этого метода декоратор @staticmethod
'''

class MyClass:
    def __init__(self, number):
        self.divider = 2
        self.number = int(number)

    def binary(self):
        return bin(self.number//self.divider)

    def __str__(self):
        return f"Результат целочисленного деления числа {self.number} на {self.divider}  - {self.binary()}"

    @staticmethod
    def strtobin(string):
        return string.replace("0b", "")


a = MyClass(11.999)
b = a.binary()
c = a.strtobin(b)
print(c)