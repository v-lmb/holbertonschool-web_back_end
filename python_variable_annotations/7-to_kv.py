#!/usr/bin/env python3
"""
Summary
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function to_kv
    """
    result: Tuple[str, float] = (k, v**2)
    return (result)
