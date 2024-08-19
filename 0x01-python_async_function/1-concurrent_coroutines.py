#!/usr/bin/env python3
"""Contains a method for calling wait_random muliple times"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls wait_random n times, returning a list of random floats of length n

    Args:
        n(int)
        max_delay(int)

    Returns:
        list of random delays
    """

    r = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(r)
