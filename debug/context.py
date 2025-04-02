import logging
from contextlib import asynccontextmanager
import asyncio

logger = logging.getLogger("jarvis")

@asynccontextmanager
async def log_context(message: str):
    logger.info(f"↪ START: {message}")
    try:
        yield
    finally:
        logger.info(f"↩ END: {message}")