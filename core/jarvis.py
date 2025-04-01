from .router import Router

class JarvisCore:
    def __init__(self):
        self._router = Router()
        
    def process_input(self, text: str) -> str: # text param will be text in future not just a command
        return self._router.handle_command(text)