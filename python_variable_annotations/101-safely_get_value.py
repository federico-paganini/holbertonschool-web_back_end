#!/usr/bin/env python3
"""Safely get a value from a dictionary with a default fallback.
This module provides a function to retrieve a value from a dictionary
using a specified key, returning a default value if the key is not found.
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[T, Any]:
    """
    Safely retrieves a value from a dictionary.
    If the key is not found, returns the default value.
    Args:
        dct (Mapping): The dictionary to search.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None]): The value to return if the key is not found.
    Returns:
        Union[T, Any]: The value associated with the key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
