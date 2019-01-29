# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    lst = str(number).split(".")
    dec = lst[1]
    if len(dec) <= ndigits:
        return number
    else:
        new_dec = dec[:ndigits]
        if int(dec[ndigits+1]) > 5:
            new_dec = int(new_dec) + 1
            return float(lst[0] + "." + str(new_dec))
        else:
            return float(lst[0] + "." + new_dec)


print(my_round(2.123456997, 3))
print(my_round(2.1999967, 5))
print(my_round(2.9967777, 5))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

path1 = os.path.join("data", "workers")
path2 = os.path.join("data", "hours_of")

with open(path2, "r", encoding="UTF-8") as f:
    hours = f.read().split("\n")
f.close()

print("Имя       \tФамилия   \tВыплата")

with open(path1, "r", encoding="UTF-8") as f1:
    for line1 in f1:
        lst = line1.split()
        dic1 = {"Name": lst[0], "Surname": lst[1], "Salary": lst[2], "Post": lst[3], "Norm": lst[4]}
        for elem in hours:
            if dic1["Name"] in elem and dic1["Surname"] in elem and dic1["Name"] != "Имя":
                norm = int(dic1["Norm"])
                real = int(elem.split()[2])
                salary = int(dic1["Salary"])
                if real == norm:
                    payout = real
                    print(f"{dic1['Name']:<10}\t{dic1['Surname']:<10}\t{payout}")

                elif real < norm:
                    payout = salary * real/norm
                    print(f"{dic1['Name']:<10}\t{dic1['Surname']:<10}\t{payout}")
                else:
                    payout = salary + salary*(real - norm)*2/norm
                    print(f"{dic1['Name']:<10}\t{dic1['Surname']:<10}\t{payout}")

f1.close()

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


alphabet = []
dic = {}
lst = []
for letter in range(ord('А'), ord('Я') + 1):
    alphabet.append(chr(letter))
    dic[chr(letter)] = []

path = os.path.join("data", "fruits.txt")

with open(path, "r", encoding="UTF-8") as f:
    for line in f:
        if len(line) > 1:
            dic[line[0]].append(line)
            if line[0] not in lst:
                lst.append(line[0])

for letter in lst:
    filename = os.path.join("data", "fruits_" + letter)
    f1 = open(filename, 'a', encoding="UTF-8")
    for fruit in dic[letter]:
        f1.write(fruit)

f.close()
f1.close()
