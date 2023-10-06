#!/usr/bin/env python3
"""A Function that sums mixed list of integers and floats"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats and
    return the result as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and
        floats to be summed.

    Returns:
        float: The sum of the input list as a float.
    """
    return float(sum(mxd_lst))
