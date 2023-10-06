#!/usr/bin/env python3
"""Type Annotation"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on a tuple by repeating each element a specified number of times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers to be zoomed in on.
        factor (int, optional): The zoom factor. Each element in the tuple
        will be repeated
            'factor' times. Defaults to 2.

    Returns:
        List[int]: A list containing the zoomed-in elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
