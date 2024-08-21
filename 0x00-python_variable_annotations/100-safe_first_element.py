#!/usr/bin/env python3
"""Contains a method for safely returning the first method of a sequence"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence or None otherwise"""
    if lst:
        return lst[0]
    else:
        return None
