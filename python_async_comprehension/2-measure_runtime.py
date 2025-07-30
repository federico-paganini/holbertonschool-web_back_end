#!/usr/bin/env python3
"""
This module provides a coroutine to measure the runtime
of executing multiple asynchronous comprehensions concurrently.
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension

async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension()
    four times concurrently using asyncio.gather.

    Returns:
        float: The total elapsed time in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = time.perf_counter()
    
    return end_time - start_time
