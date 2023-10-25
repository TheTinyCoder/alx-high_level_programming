#!/usr/bin/python3
"""
Multiplies two matrices with numpy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    matrix multiplication function
    Args:
        m_a (list of lists of integers or floats)
        m_b (list of lists of integers or floats)
    Returns:
        result matrix
    """
    return (np.dot(m_a, m_b))
