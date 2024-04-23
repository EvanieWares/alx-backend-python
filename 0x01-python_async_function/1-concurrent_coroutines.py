#!/usr/bin/env python3
"""
This module provides an asynchronous routine for managing multiple random
delays concurrently.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """
    Asynchronous routine that spawns wait_random n times with a specified
    max_delay.

    Parameters:
    - n (int): The number of times to spawn wait_random.
    - max_delay (int, optional): The maximum delay in seconds for each
    wait_random call. Defaults to 10.

    Returns:
    - list[float]: List of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    delays.sort()
    return delays
