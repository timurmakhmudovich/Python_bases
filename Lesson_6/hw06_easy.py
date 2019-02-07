'''
Задача-1: Написать класс, например, Worker, который должен содержать информацию
о работнике (ФИО, оклад, надбавка за напряженность).
Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
оклад и надбавки). Оклад и надбавку передать в виде строки.
На основе строки создать атрибут income, который реализовать в виде словаря
и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.
Применить к экземпляру
класса метод __dict__ и проверить какой будет результат применения этого метода.
А комментариях к заданию написать тип результата на русском языке.
'''

class Worker:
    def __init__(self, name, surname, patronymic, total):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.total = total
        self._income = {"salary": self.total.split("+")[0], "bonus": self.total.split("+")[1]}

worker1 = Worker("Василий", "Иванович", "Петров", "99999+5000")
worker2 = Worker("Игнат", "Давидович", "Лейпциг", "55000+33000")

print(worker1.__dict__)
#Тип сорварь. Содержит пары название-значение всех атрибутов

'''
Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
Position (реализовать наследование). Добавить классу уникальный атрибут -
% премии к зарплате (от суммы оклада).
Создать метод расчета зарплаты с учетом только премии.
Реализовать обращение к этому атриубуту, как к свойству.
Проверить работу всей структуры на реальных данных, вывести результаты.
'''

class Position(Worker):
    def __init__(self, name, surname, patronymic, total):
        Worker.__init__(self, name, surname, patronymic, total)
        self.procent = float(self._income["bonus"])/(float(self._income["salary"]) + float(self._income["bonus"]))

    @property
    def salary(self):
        total = float(self._income["salary"]) + float(self._income["bonus"])
        return total * (1 - self.procent)


worker3 = Position("Василий", "Иванович", "Петров", "99999+5000")
print(worker3.salary)

'''
Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
использования знака + в методах 1) вывода полного имени работника и возраста
2) вычисления общего дохода работника с учетом надбавки .
Проверить работу всей структуры на реальных данных, вывести результаты.
'''

class Worker2(Worker):
    def __init__(self, name, surname, patronymic, age, total):
        Worker.__init__(self, name, surname, patronymic, total)
        self.age = age

    @property
    def fio(self):
        return "Full name and age: " + self.name + " " + self.surname + " " + self.patronymic + " " + str(self.age)

    @property
    def summa(self):
        return float(self._income["salary"]) + float(self._income["bonus"])

worker4 = Worker2("Василий", "Иванович", "Петров", 56, "99999+5000")
print(worker4.fio)
print(worker4.summa)


