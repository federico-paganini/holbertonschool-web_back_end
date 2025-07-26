#!/usr/bin/env python3
"""
This module defines a function make_multiplier
that creates a multiplier function.
The multiplier function takes a number and returns
it multiplied by the given multiplier.
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies its
    input by the given multiplier.

    Args:
        multiplier (float): The multiplier to apply.

    Returns:
        function: A function that takes a number and returns
        it multiplied by the multiplier.
    """
    def multiply(value: float) -> float:
        return value * multiplier

    return multiply
