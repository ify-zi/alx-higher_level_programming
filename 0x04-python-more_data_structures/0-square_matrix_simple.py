#!/usr/bin/python3
def square_matrix_simple(my_list=[]):
    res = []
    inner = []
    for i in my_list:
        for j in i:
            j = j**2
            inner.append(j)
        res.append(inner)
        inner = []
    return res
