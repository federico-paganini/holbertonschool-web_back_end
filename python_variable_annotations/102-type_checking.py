#!/usr/bin/env python3
"""
This module demonstrates type checking with variable annotations in Python.
It defines a function `zoom_array` that takes a tuple and an optional factor,
and returns a list with elements repeated according to the factor.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the elements of a tuple by repeating each element
    a specified number of times.
    Args:
        lst (Tuple): The input tuple containing elements to zoom in on.
        factor (int): The number of times to repeat each element. Default is 2.
    Returns:
        List: A list containing the zoomed-in elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


tupla = (12, 72, 91)

zoom_2x = zoom_array(tupla)

zoom_3x = zoom_array(tupla, 3)
