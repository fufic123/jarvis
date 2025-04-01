from .base import Plugin, register_plugin

@register_plugin
class EchoPlugin(Plugin):
    _name = '/yo'
    _aliases = []
    
    def run(self):
        return 'Hello World'