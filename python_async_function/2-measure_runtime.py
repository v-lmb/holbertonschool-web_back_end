#!/usr/bin/env python3
"""
Summary
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function measure_time
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    execution_time = end - start
    return (execution_time / n)
