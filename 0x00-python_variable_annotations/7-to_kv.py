#!/usr/bin/env python3
"""Contains a funtion for creating a tuple from arguments"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of (k, v squared)"""
    return (k, v**2)
