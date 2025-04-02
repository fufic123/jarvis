from .base import Plugin, register_plugin
from debug.decorators import log_call
from debug.context import log_context

@register_plugin
class EchoPlugin(Plugin):
    _name = '/echo'
    _aliases = []
    
    @log_call
    def run(self):
        with log_context("Executing /echo command"):
            return '200'