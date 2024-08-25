#!/usr/bin/env python3
"""This code is validated using mypy and corrected accordingly"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Repeats each element of lst factor times

    Args:
        lst: a tuple of ints
        factor

    Returns:
        A list with each element of lst repeated factor times
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
