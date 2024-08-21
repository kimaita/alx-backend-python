#!/usr/bin/env python3
"""Contains a function for mapping an iterable to a list"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a tuple of (sequence, length) from an iterable lst"""
    return [(i, len(i)) for i in lst]
