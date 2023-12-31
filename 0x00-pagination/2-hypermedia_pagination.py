#!/usr/bin/env python3

"""
This module contains a function called index_range which calculates
the start and end indexes for a given page and page size, and a class
called Server that paginate a database of popular baby names.
"""
from typing import List, Dict
import math
import csv


def index_range(page, page_size):
    """Calculates the start and end indexes for a given page and page size.
    Args:
            page (int): The desired page number.
            page_size (int): The number of items to be displayed on each page.

    Return:
            tuple: A tuple containing the start and end indexes.

    Examle:
            >>> index_range(2, 10)
            (10, 20)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list containing the items on the specified page.

        Raises:
            AssertionError: if `page` or `page_size` is not an integer, or
            if `page` or `page_size` is less than or equal to 0.
        """
        assert isinstance(page, int) and isinstance(page_size, int),\
            "Page and page_size must be integers."
        assert page > 0 and page_size > 0,\
            "Page and page_size must be greater than 0."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieves hyperdata for a specific page from the dataset.

        Args:
            page (int): The page number to retrieve. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
                dict: A dictionary containing the hyperdata for the
                specified page.
        """
        dataset_page = self.get_page(page, page_size)
        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)

        hyperdata = {
            'page_size': len(dataset_page),
            'page': page,
            'data': dataset_page,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hyperdata
