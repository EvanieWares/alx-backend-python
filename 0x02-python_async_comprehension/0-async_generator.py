#!/usr/bin/env python3
"""
Module: 0-async

This module provides an asynchronous generator coroutine that yields random
numbers between 0 and 10 after waiting for 1 second.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random number between 0 and 10 after
    waiting for 1 second, repeated 10 times.

    Yields:
    - float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
