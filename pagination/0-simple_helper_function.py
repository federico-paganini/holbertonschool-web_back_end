#!/usr/bin/env python3
"""
Pagination utility module.

This module provides helper functions for calculating index ranges
commonly used in paginated data retrieval. It is designed to be
simple, clear, and reusable across different projects.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): Current page number (1-based index).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
                         and end index (exclusive) for slicing.
    """
    start = (page - 1) * page_size
    end = page_size * page
    return (start, end)
