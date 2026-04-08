#!/usr/bin/env python3
"""
Summary
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function make_multiplier
    """
    def multi(x: float) -> float:
        return x * multiplier
    return multi
