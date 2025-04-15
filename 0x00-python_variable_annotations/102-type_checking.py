#!/usr/bin/env python3
"""12. Type Checking"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Use mypy to validate the following piece of code and apply any necessary
    changes.
    """
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)
