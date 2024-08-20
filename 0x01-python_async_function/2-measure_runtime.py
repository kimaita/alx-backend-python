#!/usr/bin/env python3
"""Contains a method for measuring execution time for wait_n"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average delay from calling wait_n.
    n and max_delay are passed on to wait_n.

    Args:
        n(int)
        max_delay(int)

    Returns:
        float: total_time/n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    done = time.time()

    return (done - start) / n
