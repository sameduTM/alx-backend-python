#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""
from typing import Sequence, Any, Union, Optional
from types import NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """The types of the elements of the input are not know
    """
    if lst:
        return lst[0]
    else:
        return None
