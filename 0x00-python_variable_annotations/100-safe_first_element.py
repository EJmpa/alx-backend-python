#!/usr/bin/env python3
"""Type Annotation"""

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieve the first element from a sequence.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Union[Any, None]: The first element from the sequence, or
        None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
