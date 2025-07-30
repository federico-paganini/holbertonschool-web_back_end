#!/usr/bin/env python3
from typing import Generator
import random
import asyncio
"""
This module defines an asynchronous generator that yields random numbers
after asynchronously waiting for 1 second on each iteration.

The `async_generator` coroutine loops 10 times, each time awaiting an
asynchronous 1-second delay, then yielding a random float between 0 and 10.
It can be used to simulate a stream of random data in an asynchronous context.
It can be useful for testing asynchronous code that processes streams of data.
It is designed to be used with `async for` to consume the generated values.
"""


async def async_generator() -> Generator[float, None, None]:
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
