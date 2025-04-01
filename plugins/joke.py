from .base import Plugin, register_plugin

@register_plugin
class EchoPlugin(Plugin):
    _name = '/joke'
    _aliases = []
    
    def run(self):
        return 'he-he-he'