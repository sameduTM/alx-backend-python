#!/usr/bin/env python3
"""a type-annotated function add that takes a float a and a float b as
arguments and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """Add two float numbers and return their sum.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b
