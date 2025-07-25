#!/usr/bin/env python3
"""This module provides a simple concatenation function.

It exports a single function:
    - concat(a, b): Returns the concatenation of two strings.

Intended for basic string operations or as
a utility function in larger programs.
"""


def concat(a: str, b: str) -> str:
    """Return the concatenation of a and b.

    Args:
        a (str): The first string to concatenate.
        b (str): The second string to concatenate.

    Returns:
        str: The result of a + b.
    """
    return a + b
