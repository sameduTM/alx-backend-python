#!/usr/bin/python3
"""Use mypy to validate the following piece of code and apply any
necessary changes.
"""
from typing import Sequence, Tuple


def zoom_array(lst: Sequence, factor: int = 2) -> Tuple:
    """Zooms in on the elements of a sequence by repeating them.

    Args:
        lst (Sequence): The sequence of elements to zoom in on.
        factor (int, optional): The factor by which to zoom in (default is 2).

    Returns:
        Tuple: A tuple containing each element of `lst` repeated `factor`
        times.
    """
    zoomed_in = tuple(item for item in lst for _ in range(factor))
    return zoomed_in
