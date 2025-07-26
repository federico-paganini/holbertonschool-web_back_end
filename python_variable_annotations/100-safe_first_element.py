#!/usr/bin/env python3
"""
Safe first element of a list with type annotations.
This module provides a function to safely retrieve
the first element of a list,
returning None if the list is empty.
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a list if it exists,
    otherwise returns None.
    :param lst: List from which to retrieve the first element
    :return: The first element of the list or None if the list is empty
    """
    if lst:
        return lst[0]
    else:
        return None
