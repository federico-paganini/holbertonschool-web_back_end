#!/usr/bin/env python3
"""
This module defines a function to_kv that takes a key and a value,
squares the value, and returns a tuple containing the key and the squared value.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a key and value into a tuple."""
    return (k, float(v**2))
