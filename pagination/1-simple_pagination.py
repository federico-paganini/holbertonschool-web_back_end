#!/usr/bin/env python3
"""
pagination.py

Module to paginate a dataset of popular baby names.

Functions:
    - index_range(page, page_size): Calculates start and end
    indexes for pagination.

Classes:
    - Server: Provides methods to access the baby names
    dataset in a paginated way.
"""
import csv
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        return data[start:end] if start < len(data) else []
