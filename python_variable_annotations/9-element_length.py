#!/usr/bin/env python3
"""
Summary
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function element_lenght
    """
    return [(i, len(i)) for i in lst]
