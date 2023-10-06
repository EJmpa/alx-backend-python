#!/usr/bin/env python3
"""A function that takes list of floats and returns their sum"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats and return the result.

    Args:
        input_list (List[float]): A list of floats to be summed.

    Returns:
        float: The sum of the input list as a float.
    """
    return sum(input_list)
