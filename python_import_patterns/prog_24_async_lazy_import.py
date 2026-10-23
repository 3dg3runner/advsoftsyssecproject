# Program Name: prog_24_async_lazy_import.py
# Description: Asynchronous Lazy Loading Task - Performs lazy import in async coroutine.

import asyncio

async def run_task():
    import math
    await asyncio.sleep(0.01)
    return math.sqrt(49)

print(asyncio.run(run_task()))