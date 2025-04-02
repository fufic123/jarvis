import plugins
import difflib
import asyncio

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
        
    async def handle_command(self, command: str) -> str:
        async with log_context("Routing Command"):
            await self.log(f"Raw input: {command}")
            command = command.strip()

            if not command:
                return "Empty command."

            args = command.split()
            cmd = args[0].lower()
            params = args[1:]
            
            await self.log(f"Parsed command: {cmd}")
            await self.log(f"Parsed args: {params}")
            
            if cmd == "/help":
                if params:
                    if params[0][0] != "/": 
                        params[0] = "/" + params[0]
                    await self.log(f"Corrected param: {params[0]}", level="warning")
                    plugin = self._plugin_map.get(params[0])
                    if plugin:
                        await self.log(f"Matched plugin: {plugin.__class__.__name__}")
                        return f"{plugin.name}: {plugin.description}"
                    else:
                        await self.log(f"Unknown Command: {command}", level="warning")
                return await self._get_help()


            plugin = self._plugin_map.get(cmd)
            if plugin:
                await self.log(f"Matched plugin: {plugin.__class__.__name__}")
                return await plugin.run(params)
            await self.log(f"Unknown Command: {command}", level="warning")

            similar_commands = difflib.get_close_matches(cmd, self._plugin_map.keys(), n=1, cutoff=0.6)
            if similar_commands:
                await self.log(f"Found correct command: {similar_commands[0]}", level="warning")
                return f"Maybe you mean: {similar_commands[0]}"
            else:
                return f"Unknown Command: {command}"
            
        
    async def _get_help(self) -> str:
        lines = ["Available commands:"]
        unique_plugins = set(self._plugin_map.values())

        for plugin in unique_plugins:
            aliases = plugin.aliases
            alias_str = f" (aliases: {', '.join(aliases)})" if aliases else ""
            lines.append(f" - {plugin.name}{alias_str}: {plugin.description}")
        
        return "\n".join(lines)