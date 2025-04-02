import logging
import asyncio

logger = logging.getLogger("jarvis")

class DebugMixin:
    async def log(self, message: str, level: str = "debug"):
        log_func = getattr(logger, level.lower(), logger.info)
        log_func(f"[{self.__class__.__name__}] {message}")