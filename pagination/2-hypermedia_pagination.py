#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import Dict, List


def index_range(page: int, page_size: int) -> tuple:
    """
    function index_range
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """
    Server class
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize Server
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        function dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        function get_page
        """
        assert isinstance(page, int) and isinstance(page_size, int), \
            "page and page_size must be integers"
        assert page > 0 and page_size > 0, \
            "page and page_size must be greater than 0"

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        function get_hyper
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
