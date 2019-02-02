# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys


def mkdirs():
    for i in range(1, 10):
        try:
            os.mkdir("dir_" + str(i))
        except:
            print("Не удалось создать директорию dir_" + str(i))

def rmdirs():
    for i in range(1, 10):
        try:
            os.rmdir("dir_" + str(i))
        except:
            print("Не удалось удалить директорию dir_" + str(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

#только для папок:
def lsd():
    dirs = [ el for el in os.listdir() if not os.path.isfile(el) ]
    for dir in dirs:
        print(dir)

#содержимое директории для normal
def ls():
    files = [ el for el in os.listdir() ]
    for file in files:
        print(file)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS

def copy():
    name = sys.argv[0]
    backup = name + ".backup"
    command = "cp " + name + " " + backup
    os.system(command)
