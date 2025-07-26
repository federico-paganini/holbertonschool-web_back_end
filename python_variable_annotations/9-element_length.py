#!/usr/bin/env python3
"""
Element Length:
This module defines a function that takes a list
of strings and returns a list of tuples,
where each tuple contains a string and its length.
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of strings and returns a list of tuples
    where each tuple contains a string and its length.
    """
    return [(i, len(i)) for i in lst]
