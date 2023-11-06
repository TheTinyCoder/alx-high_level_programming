#!/usr/bin/python3
"""
Pascal's Triangle Module
"""


def pascal_triangle(n):
    """
    pascal_triangle function
    Args:
        n: number of rows
    Returns:
        an empty list if n <= 0
        a list of lists of integers representing the Pascal’s triangle of n
    """
    a_list = []
    if (n <= 0):
        return a_list
    for i in range(n):
        row = []
        if (i == 0):
            row.append(1)
        else:
            a_row = a_list[i - 1]
            for j in range(len(a_row) + 1):
                if j == 0 or j == len(a_row):
                    row.append(1)
                else:
                    row.append(a_row[j] + a_row[j - 1])
        a_list.append(row)
    return a_list
