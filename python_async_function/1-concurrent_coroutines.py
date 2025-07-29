#!/usr/bin/env python3
"""
This module defines an asynchronous function that concurrently executes
multiple coroutines with randomized delays and returns their results
in the order of completion.

It uses the `wait_random` coroutine from the `0-basic_async_syntax` module.
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `n` coroutines that each wait for a
    random delay up to `max_delay` seconds.

    The coroutines are executed concurrently, and the
    results are collected in the
    order in which the coroutines complete.

    Args:
        n (int): Number of times to call the `wait_random` coroutine.
        max_delay (int): Maximum delay value passed to `wait_random`.

    Returns:
        List[float]: A list of delay values, ordered by completion time.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delay_list = []
    for result in asyncio.as_completed(coroutines):
        delay = await result
        delay_list.append(delay)
    return delay_list
