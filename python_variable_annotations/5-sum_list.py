#!/usr/bin/env python3
"""A module to sum a list of numbers using type annotations."""


def sum_list(nums: list[float]) -> float:
    """
    Sums a list of numbers.

    :param numbers: A list of float numbers to sum.
    :return: The sum of the numbers in the list.
    """
    return sum(nums)
