'''
Задание_1. Создайте свое исключение для проверки вводимого числа.
Исключение должно возбуждаться, если пользователь ввел отрицательное число.
Также предусмотрите тот, случай, что пользователь ввел не число, а строку
(здесь можно применить встроенное исключение).
'''

class NegativeNumber(Exception):
    def __init__(self, number):
        Exception.__init__(self)
        self.number = number
    def __str__(self):
        return f'{self.number} is not positive!'


def positive(a):
    if a <= 0:
        raise NegativeNumber(a)

try:
    x = int(input("Введите число: "))
    try:
        positive(x)
    except NegativeNumber as ex:
        x = ex

except ValueError:
    x = "Это не число"

print(x)



