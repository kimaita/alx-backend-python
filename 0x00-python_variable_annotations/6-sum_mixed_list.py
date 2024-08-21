#!/usr/bin/env python3
"""Contains a list summation function"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of the elements of mxd_list.

    Args
        mxd_list: list of integers and floats

    Returns
        float
    """
    return sum(mxd_list)
