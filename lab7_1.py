import math


def sort_columns_insertion(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        for i in range(1, rows):
            key = matrix[i][col]
            j = i - 1
            while j >= 0 and matrix[j][col] > key:
                matrix[j + 1][col] = matrix[j][col]
                j -= 1
            matrix[j + 1][col] = key

    return matrix


def fi_and_F(matrix):
    n = len(matrix)
    fi_values = []

    for i in range(n):
        elements = []

        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                elements.append(matrix[i][j])

        if elements:
            product = 1
            for el in elements:
                product *= el
            fi = product ** (1 / len(elements))
        else:
            fi = 0

        fi_values.append(fi)

    F = sum(fi_values)

    return fi_values, F


A = [
    [34, 45, 65, 23, 98],
    [1, -4, 67, -3, -18],
    [23, -5, -1, 94, -25],
    [2, 24, -4, 79, -63],
    [10, 29, 25, 30, -6]
]


sorted_matrix = sort_columns_insertion(A)
fi_values, F_value = fi_and_F(sorted_matrix)


print("Відсортована матриця:")
for row in sorted_matrix:
    print(row)

print("\nЗначення fi(aij):")
for i, val in enumerate(fi_values):
    print(f"fi[{i}] = {val:.3f}")

print(f"\nЗначення F(fi) = {F_value:.3f}")
