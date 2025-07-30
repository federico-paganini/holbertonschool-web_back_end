#!/usr/bin/env python3
from typing import AsyncGenerator
import random
import asyncio
"""
This module defines an asynchronous generator that yields random numbers
after asynchronously waiting for 1 second on each iteration.

The `async_generator` coroutine loops 10 times, each time awaiting an
asynchronous 1-second delay, then yielding a random float between 0 and 10.
"""

async def async_generator() -> AsyncGenerator[float]:
    """
    Asynchronous generator that yields random floats between 0 and 10.

    On each iteration (total 10), the generator awaits a 1-second
    asynchronous sleep before yielding a new random number.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
