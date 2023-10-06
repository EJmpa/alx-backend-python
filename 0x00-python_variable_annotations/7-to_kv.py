#!/usr/bin/env python3
"""A function that takes in string and int/float and returns tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string k and the square of the int/float v.

    Args:
        k (str): The input string.
        v (Union[int, float]): An integer or float.

    Returns:
        Tuple[str, float]: A tuple with k and the square of v as a float.
    """
    return (k, float(v**2))
