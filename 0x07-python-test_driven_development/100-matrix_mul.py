#!/usr/bin/python3
"""Defines a function that  multiplies
   2 matrices
"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices
       Args:
           m_a: first matrix
           m_b: second matrix
       Returns:
              Nothing
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")

    mul = [[sum(i * j for i, j in zip(row, col))
            for col in zip(*m_b)] for row in m_a]

    return (mul)
