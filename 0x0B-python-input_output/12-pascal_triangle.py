#!/usr/bin/python3
"""
============================================================
This module defines a function to generate Pascal's triangle
up to the specified number of rows
============================================================
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the specified number of rows"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                current_value = prev_row[j - 1] + prev_row[j]
                row.append(current_value)
        triangle.append(row)

    return triangle
