import logging
from .router import Router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%H:%M:%S"
)

class JarvisCore:
    def __init__(self):
        self._router = Router()
        
    def process_input(self, text: str) -> str: # text param will be text in future not just a command
        return self._router.handle_command(text)