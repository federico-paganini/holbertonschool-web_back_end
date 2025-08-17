#!/usr/bin/env python3
"""
Deletion-Resilient Hypermedia Pagination Module

This module provides a Server class to paginate a dataset of
popular baby names
in a way that is resilient to deletions. It allows retrieving pages of data
using a start index and page size, ensuring that users do not miss items even
if some entries are removed between queries.

Classes:
    Server: Handles loading the dataset, indexing it, and providing deletion-
            resilient hypermedia pagination.

Usage:
    server = Server()
    server.indexed_dataset()  # prepares the indexed dataset
    page = server.get_hyper_index(index=0, page_size=10)
"""

import csv
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Union[int, List]]:
        """
        Return a page of data resilient to deletions in the dataset.

        Args:
            index (int): Starting index to query from (default 0)
            page_size (int): Number of items to return in the page (default 10)

        Returns:
            Dict: {
            'index': starting index of this page,
            'next_index': index to use for the next page,
            'page_size': number of items returned,
            'data': list of dataset rows for this page
            }
        """
        assert type(page_size) is int and page_size > 0
        dataset = self.indexed_dataset()
        assert (
            type(index) is int and index >= 0 and index <= max(dataset.keys())
        )

        page_data = []
        next_index = None
        data_count = 0

        for key in dataset.keys():
            if key < index:
                continue
            if data_count < page_size:
                page_data.append(dataset[key])
                data_count += 1
                continue

            next_index = key
            break

        page_info = {
            "index": index,
            "next_index": next_index,
            "page_size": len(page_data),
            "data": page_data,
        }

        return page_info
