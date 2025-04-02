import plugins
from plugins.base import Plugin
from debug.mixins import DebugMixin
from debug.context import log_context

class Router(DebugMixin):
    def __init__(self):
        self._plugin_map = {}
        for plugin in Plugin.registry:
            self._plugin_map[plugin.name] = plugin
            for alias in plugin.aliases:
                self._plugin_map[alias] = plugin
        
    def handle_command(self, command: str) -> str:
        with log_context("Routing Command"):
            self.log(f"Raw input: {command}")
            command = command.strip()

            if not command:
                return "Empty command."

            args = command.split()
            cmd = args[0].lower()
            params = args[1:]

            self.log(f"Parsed command: {cmd}")
            self.log(f"Parsed args: {params}")

            plugin = self._plugin_map.get(cmd)
            if plugin:
                self.log(f"Matched plugin: {plugin.__class__.__name__}")
                return plugin.run(params)

            self.log(f"Unknown Command: {command}", level="warning")