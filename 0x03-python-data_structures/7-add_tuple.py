#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extend the tuples to have at least 2 elements, filling with 0 if necessary
    tuple_a_extended = tuple_a + (0, 0)
    tuple_b_extended = tuple_b + (0, 0)

    # Add the corresponding elements from each tuple
    result_tuple = (
        tuple_a_extended[0] + tuple_b_extended[0],
        tuple_a_extended[1] + tuple_b_extended[1]
    )

    return result_tuple
