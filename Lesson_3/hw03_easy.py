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
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    lst = list(str(ticket_number))
    lst = [int(i) for i in lst]
    sum1 = sum(lst[0:3])
    sum2 = sum(lst[3:6])
    if sum1 == sum2:
        return "Lucky"
    else:
        return "Unlucky"

print(lucky_ticket(123006))
print(lucky_ticket(123210))
print(lucky_ticket(436751))
