#!/usr/bin/env python3
"""
This module provides an asynchronous utility function
to wait for a random delay.

The main use case is for testing or simulating asynchronous behavior
with variable response times, like network calls or I/O operations.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random amount of time between
    0 and max_delay seconds.

    Args:
        max_delay (int): Maximum number of seconds to wait. Default is 10.

    Returns:
        float: The actual number of seconds the function
        waited (a float between 0 and max_delay).
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
