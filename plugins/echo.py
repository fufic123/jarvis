from .base import Plugin, register_plugin
from debug.decorators import log_call


@register_plugin
class EchoPlugin(Plugin):
    _name = '/echo'
    _aliases = []
    _description = "Echoes back the given arguments. Returns '200' if no arguments are provided."
    
    @log_call
    def run(self, args: list) -> str:
            return " ".join(args) if args else "echo"