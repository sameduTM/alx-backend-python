#!/usr/bin/python3
"""Augment the following code with the correct duck-typed annotations:
"""
from typing import Any, Iterable, Union


def safe_first_element(lst: Iterable[Any]) -> Union[Any, None]:
    """Return the first element of an iterable `lst` or `None` if empty.

    Args:
        lst (Iterable[Any]): The iterable (list, tuple, etc.) to retrieve
        the first element from.

    Returns:
        Union[Any, None]: The first element of `lst` or `None` if `lst` is
        empty.
    """
    if lst:
        return lst[0]
    else:
        return None
