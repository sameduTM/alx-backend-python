#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """return the list of all the delays (float values)"""
    delays_list = []
    for _ in range(n):
        delays = await asyncio.gather(wait_random(max_delay))
        delays_list += delays
    return delays_list
