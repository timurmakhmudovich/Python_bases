# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    lst = [1, 1]
    for i in range(2, m+1):
        lst.append(lst[i-1] + lst[i-2])

    return lst[n:m+1]

print(fibonacci(3, 5))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for j in range(1, len(origin_list)):
        for i in range(1, len(origin_list)):
            if origin_list[i - 1] > origin_list[i]:
                origin_list[i - 1], origin_list[i] = origin_list[i], origin_list[i - 1]
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

#Задача-3:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(a, b, c, d):
    if (c[0] - a[0]) == 0:
        kac = float('inf')
    else:
        kac = (c[1] - a[1])/(c[0] - a[0])
    if (b[0] - a[0]) == 0:
        kab = float('inf')
    else:
        kab = (b[1] - a[1])/(b[0] - a[0])
    if (d[0] - a[0]) == 0:
        kad = float('inf')
    else:
        kad = (d[1] - a[1])/(d[0] - a[0])
    if (c[0] - b[0]) == 0:
        kbc = float('inf')
    else:
        kbc = (c[1] - b[1])/(c[0] - b[0])
    if (d[0] - b[0]) == 0:
        kbd = float('inf')
    else:
        kbd = (d[1] - b[1])/(d[0] - b[0])
    if (d[0] - c[0]) == 0:
        kcd = float('inf')
    else:
        kcd = (d[1] - c[1])/(d[0] - c[0])

    lst1 = [kac, kab, kad, kbc, kbd, kcd]
    lst2 = []

    for i in lst1:
        lst2.append(lst1.count(i))
    if lst2.count(2) == 4:
        return "It is a parallelogram!"
    else:
        return "It is NOT a parallelogram!"


a = (1, 1)
b = (2, 1)
c = (1, 4)
d = (2, 4)

print(is_parallelogram(a, b, c, d))
