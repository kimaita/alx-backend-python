#!/usr/bin/env python3
"""Contains a method that returns a random float"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """An asynchronous coroutine that waits for a random delay and returns it.

    The delay is between 0 and max_delay seconds long.

    Args:
        max_delay(int)

    Returns:
        delay(float)
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
