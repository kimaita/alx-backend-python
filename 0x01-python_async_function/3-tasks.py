#!/usr/bin/env python3
"""Contains a funtion for creating a concurrent Task"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio Task from wait_random

    Args:
        max_delay(int)

    Returns:
        asyncio.Task
    """

    return asyncio.create_task(wait_random(max_delay))
