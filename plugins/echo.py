from .base import Plugin, register_plugin

@register_plugin
class EchoPlugin(Plugin):
    _name = '/echo'
    _aliases = []
    
    def run(self):
        return '200'