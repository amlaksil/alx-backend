#!/usr/bin/env python3

"""
This module contains a class called Server that paginate a
database of popular baby names.
"""
from typing import List, Dict
import math
import csv


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0 """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves hyperdata for a specific index page from the dataset.

        Args:
            index (int): The start index to retrieve. Defaults to None.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            dict: A dictionary containing the hyperdata for the specified
            index page.

        Raises:
            AssertionError: If `index` is not an integer, or if `index`
            is less than 0.

        """
        assert index is None or index >= 0, "Invalid index value"

        dataset = self.indexed_dataset()
        dataset_length = len(dataset)

        if index is None:
            index = 0
        else:
            assert index < dataset_length, "Invalid index value"

        data = []
        if index in dataset:
            data.append(dataset[index])

        next_index = index + page_size
        if next_index >= dataset_length:
            next_index = None

        for i in range(index + 1, min(next_index, dataset_length)):
            if i in dataset:
                data.append(dataset[i])

        # Check if the first index was removed
        if index not in dataset:
            if next_index is not None and next_index in dataset:
                # Adjust next_index if the previous next_index was removed
                next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
