import asyncio

from .base import Plugin, register_plugin
from debug.decorators import log_call

@register_plugin
class NotifyPlugin(Plugin):
    @log_call
    async def run(self, args: list) -> str:
        if args:
            message = " ".join(args)
            return message