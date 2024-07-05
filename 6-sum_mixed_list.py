#!/usr/bin/python3
"""a type-annotated function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and float numbers.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats to sum.

    Returns:
        float: The sum of the list of numbers.
    """
    return float(sum(mxd_lst))
