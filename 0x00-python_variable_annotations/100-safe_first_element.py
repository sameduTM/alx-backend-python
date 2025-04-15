#!/usr/bin/env python3
from typing import Sequence, Any, Union, Optional
from types import NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    if lst:
        return lst[0]
    else:
        return None
