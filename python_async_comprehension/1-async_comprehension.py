#!/usr/bin/env python3
"""
Module: 1-async_comprehension
Consumes values from an asynchronous generator and returns them as a list.
"""
from typing import List
import asyncio
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random floats from the async_generator
    using async comprehension.

    Returns:
        List[float]: A list of 10 floats yielded
        by the asynchronous generator.
    """
    results = []
    async for values in async_generator():
        results.append(values)

    return results
