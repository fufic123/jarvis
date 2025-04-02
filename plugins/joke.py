from .base import Plugin, register_plugin
from debug.decorators import log_call

@register_plugin
class EchoPlugin(Plugin):
    _name = '/joke'
    _description = "Responds with a simple joke: 'he-he-he'."
    
    @log_call
    def run(self, args: list) -> str:
        return 'he-he-he'