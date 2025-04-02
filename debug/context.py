import logging
from contextlib import contextmanager

logger = logging.getLogger("jarvis")

@contextmanager
def log_context(message: str):
    logger.info(f"↪ START: {message}")
    try:
        yield
    finally:
        logger.info(f"↩ END: {message}")