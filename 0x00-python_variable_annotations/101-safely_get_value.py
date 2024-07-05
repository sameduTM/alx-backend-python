#!/usr/bin/env python3
"""Given the parameters and the return values, add type annotations to the
function

Hint: look into TypeVar

"""
from typing import TypeVar, Dict, Optional

KT = TypeVar('KT')  # Type variable for dictionary keys
VT = TypeVar('VT')  # Type variable for dictionary values


def safely_get_value(dct: Dict[KT, VT], key: KT,
                     default: Optional[VT] = None) -> Optional[VT]:
    """Safely get a value from a dictionary `dct` based on `key`.

    Args:
        dct (Dict[KT, VT]): The dictionary-like object.
        key (KT): The key to lookup in `dct`.
        default (Optional[VT], optional): Default value to return if `key` is
        not found (default is None).

    Returns:
        Optional[VT]: The value associated with `key` in `dct`, or
        `default` if `key` is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
