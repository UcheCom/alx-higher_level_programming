#!/usr/bin/python3
""" Defines a matrix division function. """


def matrix_divided(matrix, div):
    """Returns a new matrix (list of list)
    with the result of the division of matrix by div
    rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of"
                            "of integers/floats")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of"
                                "of integers/floats")

    ln_rows = []
    for row in matrix:
        ln_rows.append(len(row))
    if not all(ele == ln_rows[0] for ele in ln_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    nw_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return nw_matrix
