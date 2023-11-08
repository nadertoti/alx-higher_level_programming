#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda result: list(lambda x: x**2, result)), matrix))
