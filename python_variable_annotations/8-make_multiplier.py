#!/usr/bin/env python3
"""
Summary
"""
from typing import Tuple, Union


def make_multiplier(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function make_multiplier
    """
    result: Tuple[str, float] = (k, v**2)
    return (result)
