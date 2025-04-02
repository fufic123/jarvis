from .base import Plugin, register_plugin
from debug.decorators import log_call

@register_plugin
class EchoPlugin(Plugin):
    _name = '/yo'
    _aliases = ["/hi", "/hello"]
    _description = "Greets the user with 'Hello World'. Available via /yo, /hi, or /hello."
    
    @log_call
    def run(self, args: list) -> str:
        return 'Hello World'