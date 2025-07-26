#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of
a list of integers and floating-point numbers."""
from typing import List


def sum_mixed_list(nums: List[float | int]) -> float:
    """
    Sums a list of mixed numbers (integers and floats).

    :param nums: A list containing integers and/or floats to sum.
    :return: The total sum of all numbers in the input list.
    """
    return sum(nums)
