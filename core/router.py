import plugins
from plugins.base import Plugin

class Router:
    def __init__(self):
        self._plugins = Plugin.registry
        
    def handle_command(self, cmd: str) -> str:
        cmd = cmd.strip()
        
        for plugin in self._plugins:
            if cmd == plugin.name or cmd in plugin.aliases:
                return plugin.run()