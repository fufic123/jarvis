import logging
from contextlib import asynccontextmanager
import asyncio

logger = logging.getLogger("jarvis")

@asynccontextmanager
async def log_context(message: str):
    logger.context(f"↪ START: {message}")
    try:
        yield
    finally:
        logger.context(f"↩ END: {message}")