#!/usr/bin/env python3
"""
This module provides a utility function to create an asyncio Task
that runs the wait_random coroutine from the '0-basic_async_syntax' module.

It allows scheduling the asynchronous wait_random task without
requiring the caller to be inside an async function.
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Create and return an asyncio.Task that runs wait_random with max_delay.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: The scheduled asyncio Task.
    """
    return asyncio.create_task(wait_random(max_delay))
