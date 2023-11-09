#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sqr = []
    if matrix:
        for i in matrix:
            sq = []
            for j in i:
                sq.append(j ** 2)
            sqr.append(sq)
    return sqr
