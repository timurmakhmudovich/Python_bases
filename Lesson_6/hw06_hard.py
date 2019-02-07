'''
Задание-1: Решите задачу:

Дана ведомость расчета заработной платы (файл "data/workers").
Рассчитайте зарплату всех работников, зная что они получат полный оклад,
если отработают норму часов. Если же они отработали меньше нормы,
то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
удвоенную ЗП, пропорциональную норме.
Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

С использованием классов.
Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
каждый работник получал строку из файла

'''

import os


class Worker:
    def __init__(self, worker):
        self.worker = worker.split()

    def payout(self, hours):
        lst1 = self.worker
        for el in hours:
            if lst1[0] in el and lst1[1] in el:
                if lst1[0] == "Имя":
                    print("{:<10}{:<10}Выплата".format('Имя','Фамилия'))
                else:
                    lst2 = el.split()
                    name = lst1[0]
                    surname = lst1[1]
                    salary = int(lst1[2])
                    norm = int(lst1[4])
                    real = int(lst2[2])

                    if real == norm:
                        payout = real
                    elif real < norm:
                        payout = salary * real / norm
                    else:
                        payout = salary + salary * (real - norm) * 2 / norm

                    print(f"{name:<10}{surname:<10}{payout}")


path1 = os.path.join("data", "workers")
path2 = os.path.join("data", "hours_of")

with open(path1, 'r', encoding="UTF-8") as f:
    workers = f.readlines()

with open(path2, 'r', encoding="UTF-8") as f:
    hours = f.readlines()




for data in workers:
    worker = Worker(data)
    worker.payout(hours)

