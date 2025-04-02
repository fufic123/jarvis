import plugins
import difflib

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
            
            if cmd == "/help":
                if params:
                    if params[0][0] != "/": 
                        params[0] = "/" + params[0]
                    self.log(f"Corrected param: {params[0]}", level="warning")
                    plugin = self._plugin_map.get(params[0])
                    if plugin:
                        self.log(f"Matched plugin: {plugin.__class__.__name__}")
                        return print(f"{plugin.name}: {plugin.description}")
                    else:
                        self.log(f"Unknown Command: {command}", level="warning")
                return print(self._get_help())


            plugin = self._plugin_map.get(cmd)
            if plugin:
                self.log(f"Matched plugin: {plugin.__class__.__name__}")
                return plugin.run(params)
            self.log(f"Unknown Command: {command}", level="warning")

            similar_commands = difflib.get_close_matches(cmd, self._plugin_map.keys(), n=1, cutoff=0.6)
            if similar_commands:
                self.log(f"Found correct command: {similar_commands[0]}", level="warning")
                return print(f"Maybe you mean: {similar_commands[0]}")
            else:
                return print(f"Unknown Command: {command}")
            
        
    def _get_help(self) -> str:
        lines = ["Available commands:"]
        unique_plugins = set(self._plugin_map.values())

        for plugin in unique_plugins:
            aliases = plugin.aliases
            alias_str = f" (aliases: {', '.join(aliases)})" if aliases else ""
            lines.append(f" - {plugin.name}{alias_str}: {plugin.description}")
        
        return "\n".join(lines)