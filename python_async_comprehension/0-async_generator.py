#!/usr/bin/env python3
"""
This module contains an async generator that yields random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async generator that loops 10 times, waits 1 second each time,
    and yields a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
