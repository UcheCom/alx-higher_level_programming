#!/usr/bin/python3
"""Defines a function lazy_matrix_mul
Matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies m_a and m_b using
    matmul, and returns the result.

    Args:
           m_a: first matrix
           m_b: second matrix
    """
    return np.matmul(m_a, m_b)
