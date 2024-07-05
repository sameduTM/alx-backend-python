#!/usr/bin/env python3
"""Annotate the below function-s parameters and return values with the
appropriate types
"""
from typing import List, Tuple, Union


def element_length(lst: List[Union[str,
                                   List]]) -> List[Tuple[Union[str,
                                                               List],
                                                         int]]:
    return [(i, len(i)) for i in lst]
