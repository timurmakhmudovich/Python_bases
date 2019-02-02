# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <dir_name> - меняет текущую директорию на одну из внутренних
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# ИСПОЛЬЗОВАТЬ МОДУЛИ SYS, OS, SHUTIL

import os
import sys
import shutil


def print_help():
    print("help - получение справки")
    print("ping - тестовый ключ")
    print("mkdir <dir_name> - создание директории")
    print("rmdir <dir_name> - удаление директории")
    print("cp <file_name> - создать копию файла")
    print("rm <file_name> - удалить указанный файл")
    print("cd <dir_name> - перейти в директорию")
    print("pwd - полный путь для текущей директории")
    print("ls - содержимое текущей директории")

def ping():
    print("pong")

def make_dir():
    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def remove_dir():
    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('директория {} не существует'.format(dir_name))
    except NotADirectoryError:
        print('Файл {} не является директорией'.format(dir_name))

def cp():
    try:
        file_name = sys.argv[2]
    except IndexError:
        file_name = None
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    new_file_name = file_name + ".backup"
    new_file_path = os.path.join(os.getcwd(), new_file_name)
    try:
        shutil.copyfile(file_path, new_file_path)
        print('Файл {} скорирован в файл {}'.format(file_name, new_file_name))
    except FileNotFoundError:
        print('Файла {} не существует'.format(file_name))

def rm():
    try:
        file_name = sys.argv[2]
    except IndexError:
        file_name = None
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    if os.path.isfile(file_path):
        answer = input("Вы точно хотите удалить файл {}? (Y/N)".format(file_name))
        if answer == "Y" or answer == "y":
            try:
                os.remove(file_path)
                print("Файл {} удален".format(file_name))
            except PermissionError:
                print("Не хватает прав на удаление файла {}".format(file_name))
        else:
            print("Удаление отменено")
    elif os.path.isdir(file_path):
        print("Это директория, а не файл")
    else:
        print('Файла {} не существует'.format(file_name))

def cd():
    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print('Успешно перешли в директорию {}'.format(dir_name))
    except NotADirectoryError:
        print('{} не является директорией'.format(dir_name))
    except FileNotFoundError:
        print('Не существует директории {}'.format(dir_name))

def pwd():
    dir = os.getcwd()
    print("Полный путь текущей директории: {}".format(dir))

def ls():
    files = [ el for el in os.listdir() ]
    for file in files:
        print(file)


do = {
    "help": print_help,
    "ping": ping,
    "mkdir": make_dir,
    "rmdir": remove_dir,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "pwd": pwd,
    "ls": ls
}

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
else:
    print_help()
