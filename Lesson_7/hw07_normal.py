'''
Задача-1: Создать класс Матрица. В конструктор класса передавать переменную
содержащую матрицу в виде списка списков. В конструкторе класса преобразовать
список списков в привычный матричный вид. Переопределить стандартное поведение
методов __add__ и __str__ класса. Создать два экземпляра класса Матрица с данными.
Метод __add__ должен реализовывать сложение матриц, а __str__ - вывод итоговой
матрицы.
'''

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            new_matrix = []
            for i in range (0, len(self.matrix)):
                new_matrix.append([])
                for j in range (0, len(self.matrix[0])):
                    new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
            return Matrix(new_matrix)
        else:
            return "Нельзя сколадывать матрицы разных размеров"

    def __str__(self):
        string = "Matrix:\n"
        for row in self.matrix:
            for el in row:
                string += str(el) + "\t"
            string += "\n"
        return string




matrix1 = Matrix([ [1,2,3], [4,5,6], [7,8,9] ])
matrix2 = Matrix( [ [0,3,5], [7,9,11], [13,15,17] ])
new_matrix = matrix1 + matrix2
print(str(new_matrix))
