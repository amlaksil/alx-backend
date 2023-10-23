#!/usr/bin/env python3

"""
This module contains a function called index_range which calculates
the start and end indexes for a given page and page size.
"""


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
