#!/usr/bin/python3
"""a type-annotated function sum_list which takes a list input_list of
floats as argument and returns their sum as a float."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of float numbers.

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
