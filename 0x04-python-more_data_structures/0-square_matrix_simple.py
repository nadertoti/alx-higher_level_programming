#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda submat: list(lambda x: x**2, submat)), matrix))
