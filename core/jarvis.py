import asyncio

from core.router import Router
from .logs import setup_logging


class JarvisCore:
    def __init__(self):
        setup_logging()
        self._router = Router()

    async def process_input(self, text: str) -> str:
        return await self._router.handle_command(text)