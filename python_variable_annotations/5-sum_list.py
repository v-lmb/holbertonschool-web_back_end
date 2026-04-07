#!/usr/bin/env python3
"""
Summary
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    function sum_list
    """
    result: float = 0
    for i in range(len(input_list)):
        result += input_list[i]
    return (result)
