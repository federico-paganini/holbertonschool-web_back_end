#!/usr/bin/env python3
"""
A module to sum a list of numbers using type annotations.

This module provides a function to calculate the sum of
a list of floating-point numbers.

It demonstrates the use of Python's type annotations for
improved code clarity and static analysis.

    Calculate the sum of a list of floating-point numbers.

    Args:
        nums (List[float]): A list containing float values to be summed.

    Returns:
        float: The total sum of all numbers in the input list.

    Example:
        >>> sum_list([1.0, 2.5, 3.5])
        7.0
"""
from typing import List


def sum_list(nums: List[float]) -> float:
    """
    Sums a list of numbers.

    :param numbers: A list of float numbers to sum.
    :return: The sum of the numbers in the list.
    """
    return sum(nums)
