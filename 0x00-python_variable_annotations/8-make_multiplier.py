#!/usr/bin/env python3
"""Contains a function that returns a function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies multiplier by another float

    Args
        multiplier(float)

    Return
        Callable
    """
    return lambda x: x * multiplier
