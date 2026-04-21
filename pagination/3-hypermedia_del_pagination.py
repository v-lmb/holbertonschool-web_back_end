#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""

import csv
import math
from typing import Dict, List


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
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        function indexed_dataset
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        function get_hyper_index
        """
        indexed = self.indexed_dataset()
        assert index is not None and 0 <= index < len(self.dataset()), \
            "index is out of valid range"

        data = []
        current = index

        while len(data) < page_size:
            if current in indexed:
                data.append(indexed[current])
            current += 1
            # Safety: stop if we've gone past the original dataset length
            if current > len(self.dataset()):
                break

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": current,
        }
