#!/usr/bin/env python3
"""Type Annotation"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary by key.

    Args:
        dct (Mapping): A dictionary-like object.
        key (Any): The key to lookup in the dictionary.
        default (Union[T, None], optional): The default value to
        return if the key is not found.
            Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found, or the
        default value (or None) if not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
