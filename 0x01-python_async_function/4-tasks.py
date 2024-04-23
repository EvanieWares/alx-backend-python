#!/usr/bin/env python3
"""
This module provides an asynchronous routine to manage multiple random delay
tasks using the task_wait_random function from async_delay_manager.
"""
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> list[float]:
    """
    Asynchronous routine that spawns task_wait_random n times with a specified
    max_delay.

    Parameters:
    - n (int): The number of times to spawn task_wait_random.
    - max_delay (int, optional): The maximum delay in seconds for each
    task_wait_random call. Defaults to 10.

    Returns:
    - list[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    delays.sort()
    return delays
