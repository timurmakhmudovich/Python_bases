'''
Задание 1. Реализовать класс-строитель. В его конструктор передать два списка.
Класс должен возвратить python-объект словарь. Проверить, что объект
создается корректно - создать экземпляр класса и обратиться к значению
элемента словаря, как к атрибуту класса.
'''

class DicBuilder:
    def __init__(self, lst1, lst2):
        for i in range(len(lst1)):
            key = lst1[i]
            value = str(lst2[i])
            setattr(self, key, value)


lst1 = ['a', 'b', 'c', 'd', 'e']
lst2 = [1, 2, 3, 4, 5]

new = DicBuilder(lst1, lst2)
print(new.b)


'''
Задание 2.
Создать класс-обертку для списка. Список передвайте в конструктор класса.
Реализуйте удаление всех элементов из списка через функцию clear.
Но функция должна применяться не к списку, а к экземпляру класса.
Внутри класса должно быть предусмотрено делегирование этой функции методу (clear)
списка.
'''

class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        if attrname == "clear":
            print("Clear List")
            return getattr(self.wrapped, attrname)
        else:
            print("Reverse List")
            attrname = "reverse"
            return getattr(self.wrapped, attrname)


x = Wrapper([11, 2, 13, -5, 14, 0])
x.cleara()
print(x.wrapped)
x.clear()
print(x.wrapped)

