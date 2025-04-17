#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""
    delays_list = []
    for _ in range(n):
        delays_list += await asyncio.gather(task_wait_random(max_delay))
    for _ in range(len(delays_list)):
        for i in range(len(delays_list) - 1):
            if delays_list[i] > delays_list[i + 1]:
                temp = delays_list[i + 1]
                delays_list[i + 1] = delays_list[i]
                delays_list[i] = temp
    return delays_list
