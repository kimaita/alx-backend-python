#!/usr/bin/env python3
"""Contains a method for calling task_wait_random muliple times"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Calls task_wait_random n times,
    returning a list of random floats of length n

    Args:
        n(int)
        max_delay(int)

    Returns:
        list of random delays
    """

    r = await asyncio.gather(*(task_wait_random(max_delay) for i in range(n)))
    return sorted(r)
