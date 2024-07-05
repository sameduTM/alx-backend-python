#!/usr/bin/python3
"""a type-annotated function to_kv that takes a string k and an int OR float
v as arguments and returns a tuple. The first element of the tuple is the
string k. The second element is the square of the int/float v and should be
annotated as a float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string and the square of the given number.

    Args:
        k (str): The string.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`
                           and the second element is the square of `v`.
    """
    return k, float(v ** 2)
