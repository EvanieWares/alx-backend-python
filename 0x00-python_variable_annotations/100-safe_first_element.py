#!/usr/bin/env python3
"""
Module to demonstrate safe retrieval of the first element from a sequence.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a sequence or None
    if the sequence is empty.

    Args:
        lst (Sequence[Any]): The sequence from which to retrieve
        the first element.

    Returns:
        Union[Any, None]: The first element of the sequence,
        or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
