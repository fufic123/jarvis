import logging

logger = logging.getLogger("jarvis")

class DebugMixin:
    def log(self, message: str) -> str:
        logger.info(f"[{self.__class__.__name__}] {message}")