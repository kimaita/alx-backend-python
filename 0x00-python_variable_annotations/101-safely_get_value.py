#!/usr/bin/env python3
"""Type annotated function"""

from typing import Mapping, Any, Optional, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Optional[T] = None
) -> Union[Any, T]:
    """Safely return the value associated with `key` in `dct`

    Args:
        dct
        key
        default

    Returns:
        the value associated with key or default otherwise
    """
    if key in dct:
        return dct[key]
    else:
        return default
