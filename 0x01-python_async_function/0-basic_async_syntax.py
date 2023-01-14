#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an
integer argument (max_delay, with a default value of 10)
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Takes in an argument, waits for a random delay, returns it."""
    n: float = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
