#!/usr/bin/env python3
"""
Pagination module for loading and serving slices of a CSV dataset.

This module implements:
    - `index_range`: Calculates start and end indices for pagination.
    - `Server` class: Loads and caches a CSV dataset of popular baby names,
      with methods to retrieve specific pages and hypermedia-style metadata.

Features:
    • Caches the dataset in memory for performance.
    • Provides strict input validation (page and page_size must be positive integers).
    • Supports "hypermedia" pagination with total pages, next/previous page numbers,
      and page data.

Example:
    server = Server()
    page_data = server.get_page(2, 5)
    hyper_info = server.get_hyper(2, 5)
"""
import csv, math
from typing import List, Tuple, Dict, Union


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
    """Server class to paginate a database of popular baby names."""

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
        """
        Return a specific page of the dataset.

        Args:
            page (int): Page number (1-based index). Must be > 0.
            page_size (int): Number of items per page. Must be > 0.

        Returns:
            List[List]: A list of rows corresponding to the
            requested page.
                        Returns an empty list if the page is
                        out of range.

        Raises:
            AssertionError: If page or page_size are not integers
            greater than 0.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        return data[start:end] if start < len(data) else []

    def get_hyper(
        self, page: int = 1, page_size: int = 10
    ) -> Dict[str, Union[int, List[List], None]]:
        """
        Return pagination details and data in a hypermedia format.

        Args:
            page (int, optional): The current page number (1-based index).
                                Must be greater than 0. Defaults to 1.
            page_size (int, optional): Number of items per page.
                                    Must be greater than 0. Defaults to 10.

        Returns:
            Dict[str, Union[int, List[List], None]]:
                A dictionary containing:
                    - "page_size" (int): Number of items per page.
                    - "page" (int): Current page number.
                    - "data" (List[List]): The rows of data for the
                    current page.
                    - "next_page" (int | None): The next page number,
                    or None if this is the last page.
                    - "previous_page" (int | None): The previous page number,
                    or None if this is the first page.
                    - "total_pages" (int): Total number of available pages.

        Raises:
            AssertionError: If `page` or `page_size` are not
            positive integers.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()
        total_pages = math.ceil(len(data) / page_size)

        data = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page < total_pages else None,
            "previous_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
