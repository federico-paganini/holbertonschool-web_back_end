#!/usr/bin/env python3
"""
This module defines an asynchronous function to concurrently run multiple
asyncio.Tasks created by `task_wait_random` and gather their results in the
order of completion.

It imports `task_wait_random` from the '3-tasks' module, which schedules
individual random delay tasks.

The main coroutine, `task_wait_n`, launches `n` such tasks with a maximum
delay of `max_delay` seconds, collects their results as they complete,
and returns the list of delays.
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[asyncio.Task]:
    """
    Create and run `n` asyncio.Tasks by calling `task_wait_random` with
    `max_delay`, wait for their completion in order of finishing, and
    return the list of actual delays.

    Args:
        n (int): Number of tasks to run concurrently.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of float delay values in order of task completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay_list = []
    for result in asyncio.as_completed(tasks):
        delay = await result
        delay_list.append(delay)
    return delay_list
