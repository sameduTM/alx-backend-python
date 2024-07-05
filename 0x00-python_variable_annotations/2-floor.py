#!/usr/bin/python3
"""a type-annotated function floor which takes a float n as argument
and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """Return the floor of the given float number.

    Args:
        n (float): The number to floor.

    Returns:
        int: The floor of the number.
    """
    return math.floor(n)
