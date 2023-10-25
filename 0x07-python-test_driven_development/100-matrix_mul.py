#!/usr/bin/python3
"""
Multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """
    matrix multiplication function
    Args:
        m_a (list of lists of integers or floats)
        m_b (list of lists of integers or floats)
    Returns:
        result matrix
    Raises:
        TypeError if :
            m_a or m_b is not a list
            m_a or m_b is not a list of lists
            m_a rows are not of the same size
            m_b rows are not of the same size
            an element of those list of lists is not an int or float
            ValueError if:
                m_a or m_b is empty
                m_a and m_b can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) is 0 or all(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) is 0 or all(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if not all(type(i) in (int, float) for i in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(type(i) in (int, float) for i in row):
            raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            val = [round(m_a[i][k] * m_b[k][j], 2) for k in range(len(m_b))]
            row.append(sum(val))
        result.append(row)
    return (result)
