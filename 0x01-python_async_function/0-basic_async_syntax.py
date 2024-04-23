#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine for generating a random delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay seconds

    Parameters:
    - max_delay (int, optional): The maximum delay in seconds. Defaults to 10.

    Returns:
    - float: The random delay that was waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
