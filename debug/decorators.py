from functools import wraps
import logging
import asyncio

logger = logging.getLogger("jarvis")

def log_call(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        logger.info(f"Calling {self.__class__.__name__}.{func.__name__}() with args={args}, kwargs={kwargs}")
        result = await func(self, *args, **kwargs)
        logger.info(f"{self.__class__.__name__}.{func.__name__}() returned: {result}")
        return result
    return wrapper
