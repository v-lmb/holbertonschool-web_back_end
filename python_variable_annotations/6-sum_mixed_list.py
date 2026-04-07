#!/usr/bin/env python3
"""
Summary
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function sum_mixed_list
    """
    result: float = 0
    for i in range(len(mxd_lst)):
        result += mxd_lst[i]
    return (result)
