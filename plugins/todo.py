import asyncio

from .base import Plugin, register_plugin
from debug.decorators import log_call
from debug.context import log_context

@register_plugin
class TodoPlugin(Plugin):
    _name = "/todo"
    _description = "/Manage your task list: add, list, delete."
    
    def __init__(self):
        self.commands = {
        "add": self._add,
        "list": self._list,
        "delete": self._delete
        }
    
    @log_call
    async def run(self, args: list) -> str:
        async with log_context("Handling /todo"):
            if len(args) == 0:
                await self.log("Usage: /todo <add|list|delete> [task]", level="error")
                return "Usage: /todo <add|list|delete> [task]"
            
            sub_cmd = args[0].lower()
            handler = self.commands.get(sub_cmd)
            
            if not handler:
                await self.log(f"Unknown subcommand: {sub_cmd}.", level="error")
                return f"Unknown subcommand: {sub_cmd}. Use one of: {', '.join(self.commands)}"
            
            return await handler(args[1::])
        
    @log_call
    async def _add(self, args: list) -> str:
        task = " ".join(args)
        if not task:
            return "Please provide a task to add."
        # TODO: Add to storage
        return f"Task added: {task}"

    @log_call
    async def _list(self, args: list) -> str:
        # TODO: Load tasks
        return "Your tasks:\n1. Learn Python"

    @log_call
    async def _delete(self, args: list) -> str:
        if not args or not args[0].isdigit():
            return "Please provide a task number to delete."
        # TODO: Delete from storage
        return f"Task {args[0]} deleted."
        