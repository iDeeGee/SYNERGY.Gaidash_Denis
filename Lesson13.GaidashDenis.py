import random

def generate_matrix(rows, cols):    
    return [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix1, matrix2):
    """
    Функция для сложения двух матриц.
    """
    rows = len(matrix1)
    cols = len(matrix1[0])
    result_matrix = []

    for i in range(rows):
        result_row = []
        for j in range(cols):
            result_row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(result_row)

    return result_matrix

rows = int(input("Введите количество строк: ")) 
cols = int(input("Введите количество столбцов: "))

matrix1 = generate_matrix(rows, cols)
matrix2 = generate_matrix(rows, cols)

result_matrix = add_matrices(matrix1, matrix2)

print("\nПервая матрица:")
for row in matrix1:
    print(row)

print("\nВторая матрица:")
for row in matrix2:
    print(row)

print("\nРезультирующая матрица:")
for row in result_matrix:
    print(row)
