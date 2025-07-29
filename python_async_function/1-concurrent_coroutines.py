"""
This module provides a coroutine that executes multiple asynchronous delays in parallel.

It uses the `wait_random` coroutine from another module to simulate asynchronous tasks 
with random delays. The main function, `wait_n`, launches multiple such tasks concurrently.
"""
import asyncio
wait_random = __import__("0-basic_async_syntax.py").wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawn `n` coroutines that each wait for a random delay between 0 and `max_delay` seconds.

    The coroutines are executed concurrently using asyncio.gather.

    Args:
        n (int): Number of times to call the `wait_random` coroutine.
        max_delay (int): Maximum possible delay for each coroutine.

    Returns:
        list[float]: A list of float values representing the actual delays waited by each coroutine.
    """
    delay_list = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*delay_list)
